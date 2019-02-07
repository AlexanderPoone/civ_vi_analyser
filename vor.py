import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.cm as cm
from urllib.request import urlopen
from io import BytesIO
from PIL import Image

from scipy.spatial import Voronoi, voronoi_plot_2d

def PolygonArea(corners):
    n = len(corners) # of corners
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += corners[i][0] * corners[j][1]
        area -= corners[j][0] * corners[i][1]
    area = abs(area) / 2.0
    return area

def PolygonCentroid(arr):
    length = arr.shape[0]
    sum_x = np.sum(arr[:, 0])
    sum_y = np.sum(arr[:, 1])
    return sum_x/length, sum_y/length

places = np.array([[32.023, 27.579], [66.896, 66.705], [36.873, 4.526], [38.649, 8.425], [82.587, 35.943], [47.208, 79.508], [55.823, 60.643], [65.137, 41.615], [60.862, 35.476], [16.058, 24.762], [46.451, 13.404], [51.266, 17.862], [27.371, 6.303], [24.59, 7.89], [28.572, 10.423], [16.991, 14.351], [18.008, 12.039], [38.74, 4.491], [50.009, -2.5], [49.01, 74.87], [95.956, 68.052], [10.987, 21.765], [6.477, 10.603], [8.176, 12.63], [3.972, 12.917], [0.538, 17.229], [16.867, 6.001], [36.766, 18.165], [5.79, 24.542], [27.102, 5.201], [22.025, 1.766], [25.663, 11.132], [5.065, 2.77], [77.387, 58.362], [43.223, 54.913], [17.095, 19.372], [6.832, 13.957], [10.159, 8.579], [7.05, 12.542], [2.02, 12.873], [1.105, 1.405], [37.973, 17.201], [59.825, 27.99], [39.916, 7.588], [-0.739, 15.667], [6.405, -0.051], [36.795, 10.632], [59.974, 19.505], [83.717, 69.687], [95.008, 1.625], [59.564, 106.546], [52.988, 30.574], [32.751, 12.199], [14.616, 7.922], [44.699, 13.238], [44.467, 13.371], [5.045, 12.629], [11.311, 8.576], [-7.517, 25.863], [18.9, 5.577], [5.262, 20.076], [69.568, 60.828], [-0.798, 16.5], [40.337, 7.581], [31.018, 8.426], [76.087, 77.667], [40.334, 19.839], [38.866, 1.079], [40.44, 49.31], [51.952, 53.701], [62.919, 43.306]])
placeNames = ["Pokrovka", "Hong Kong", "Râ-Kedet", "Tyre", "Kandy", "Kyoto", "Sian", "Pataliputra", "Delhi", "Saint Petersburg", "Uruk", "Pasargadae", "Athens", "Pella", "Konstantiniyye", "Cracovie", "Buda", "Cairo", "Meroë", "Gyeongju", "Majahapit", "Stockholm", "Paris", "Aachen", "London", "Stirling", "Rome", "Tbilisi", "Niðaróss", "Sparta", "Valletta", "Preslav", "Madrid", "Angkor Thom", "Qaraqorum", "Vilnius", "Amsterdam", "Geneva", "Brussels", "Cardiff", "Lisbon", "Yerevan", "Mohenjo-daro", "Jerusalem", "Armagh", "Granada", "Antioch", "Muscat", "Bandar Brunei", "Antananarivo", "Nan Madol", "Kabul", "Hattusa", "Bologna", "Babylon", "Akkad", "Cliffs of Dover", "Matterhorn", "Eyjafjallajökull", "Mt. Vesuvius", "Lysefjord", "Hạ Long Bay", "Giant's Causeway", "Dead Sea", "Pamukkale", "Chocolate Hills", "Gobustan", "Sahara el-Beyda", "Ubsunur Hollow", "Zhangye Danxia", "Mount Everest"]
print(len(places))
print(placeNames[-15:])
places = list(map(lambda x: [x[1]*10,(100-x[0])*8.89], places))
vor = Voronoi(places[:-15])
voronoi_plot_2d(vor, show_vertices=False)

norm = mcolors.Normalize(vmin=0, vmax=50000, clip=True)
mapper = cm.ScalarMappable(norm=norm, cmap=cm.brg)

file = BytesIO(urlopen('https://upload.wikimedia.org/wikipedia/commons/b/b6/Asia_laea_relief_location_map.jpg').read())
img = Image.open(file)
plt.imshow(img.resize([1000,899]).transpose(Image.FLIP_TOP_BOTTOM),origin='upper')
for r in range(len(vor.point_region)):
    region = vor.regions[vor.point_region[r]]
    polygon = [vor.vertices[i] for i in region]
    if PolygonArea(polygon) < 200000 and not -1 in region:
    	plt.fill(*zip(*polygon), color=mapper.to_rgba(PolygonArea(polygon), alpha=0.2))
    	plt.text(vor.points[r][0], vor.points[r][1], str(int(PolygonArea(polygon))),horizontalalignment='right',verticalalignment='top')
    	tmp = PolygonCentroid(np.array(polygon))
    	plt.plot(tmp[0], tmp[1], 'w+')
    plt.text(vor.points[r][0], vor.points[r][1], placeNames[r],horizontalalignment='left')
    print(PolygonArea(polygon))
for p in range(-15, 0):
	plt.plot(places[p][0], places[p][1], 'yo')
	plt.text(places[p][0], places[p][1], placeNames[p],horizontalalignment='left')
fig = plt.gcf()
fig.set_size_inches(10, 8.89)
plt.show()

# ---------------------

places = [[35.603, 94.872], [95.856, 84.463], [29.918, 59.413], [90.02, 61.258], [83.097, 58.162], [79.739, 68.993], [59.134, 50.981], [66.256, 50.409], [34.845, 45.835], [62.834, 24.85], [58.194, 30.704], [55.257, 21.966], [42.052, 18.66], [82.07, 40.677], [66.674, 93.846], [24.516, 36.794], [92.822, 59.231], [97.848, 44.861], [75.078, 64.372], [83.654, 12.418], [45.411, 56.507], [53.834, 29.243], [70.468, 30.264], [57.823, 28.205], [54.507, 17.653], [85.6, 2.268], [70.697, 94.891], [99.647, 85.426], [45.815, 14.321], [92.139, 11.44], [87.636, 84.291], [78.96, 79.054], [99.821, 7.687], [75.16, 38.606], [56.557, 23.986], [71.183, 32.647], [16.599, 7.084], [84.78, 44.125], [36.367, 31.785], [43.533, 14.981], [100.159, 86.131], [87.666, 70.885], [66.067, 102.365]]
placeNames = ["Pokrovka", "Tyre", "Saint-Pétersbourg", "Athènes", "Pella", "Constantinople", "Kraków", "Buda", "Stockholm", "Paris", "Aix-la-Chapelle", "Londres", "Stirling", "Rome", "Tbilisi", "Niðaróss", "Sparte", "La Valette", "Preslav", "Madrid", "Vilnius", "Amsterdam", "Genève", "Bruxelles", "Cardiff", "Lisbonne", "Yerevan", "Jérusalem", "Armagh", "Grenade", "Antioche", "Hattusa", "Fez", "Bologne", "Falaises de Douvres", "Matterhorn", "Eyjafjallajökull", "Mont Vésuve", "Lysefjord", "La Chaussée des Géants", "Dead Sea", "Pamukkale", "Gobustan"]
print(len(places))
print(len(placeNames))
places = list(map(lambda x: [x[1]*10,(100-x[0])*8.55], places))
vor = Voronoi(places[:-9])
voronoi_plot_2d(vor, show_vertices=False)

norm = mcolors.Normalize(vmin=0, vmax=50000, clip=True)
mapper = cm.ScalarMappable(norm=norm, cmap=cm.brg)

file = BytesIO(urlopen('https://upload.wikimedia.org/wikipedia/commons/7/79/Europe_relief_laea_location_map.jpg').read())
img = Image.open(file)
plt.imshow(img.resize([1000,855]).transpose(Image.FLIP_TOP_BOTTOM),origin='upper')
for r in range(len(vor.point_region)):
    region = vor.regions[vor.point_region[r]]
    polygon = [vor.vertices[i] for i in region]
    if PolygonArea(polygon) < 100000 and not -1 in region:
    	plt.fill(*zip(*polygon), color=mapper.to_rgba(PolygonArea(polygon), alpha=0.2))
    	plt.text(vor.points[r][0], vor.points[r][1], str(int(PolygonArea(polygon))),horizontalalignment='right',verticalalignment='top')
    	tmp = PolygonCentroid(np.array(polygon))
    	plt.plot(tmp[0], tmp[1], 'w+')
    plt.text(vor.points[r][0], vor.points[r][1], placeNames[r],horizontalalignment='left')
    print(PolygonArea(polygon))
for p in range(-9, 0):
	plt.plot(places[p][0], places[p][1], 'yo')
	plt.text(places[p][0], places[p][1], placeNames[p],horizontalalignment='left')
fig = plt.gcf()
fig.set_size_inches(10, 10)
plt.show()