import os
import json
from functools import reduce
from math import sqrt, pow

def PolygonArea(corners):
    #uses the shoelace formula
    n = len(corners)
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += corners[i][0] * corners[j][1]
        area -= corners[j][0] * corners[i][1]
    area = abs(area) / 2.0
    return area

def PolygonPerimeter(corners):
    n = len(corners)
    dist = 0
    for i in range(n):
        j = (i + 1) % n
        dist += sqrt(pow(corners[i][0] - corners[j][0], 2) + pow(corners[i][1] - corners[j][1], 2))

    return dist

#hardcoded path I used for congressional districts in 2016, change these next 2 lines if you want to change the input
folders = os.listdir("cds/2016/")
paths = list(map(lambda x: "cds/2016/" + x + "/shape.geojson", folders))
districts = list()

for path in paths:
    with open(path) as f:
        data = json.load(f)
        coordinates = data["geometry"]["coordinates"]
        counter = 0
        #reduce the list of lists down to just the list of coordinates
        while(type(coordinates[0][0]) != float):
            coordinates = list(reduce(lambda x, y: x + y, coordinates))

        area = PolygonArea(coordinates)
        peri = PolygonPerimeter(coordinates)

        score = area/peri
        district = {"name": data["properties"]["District"], "score": score, "area": area, "peri": peri}
        districts.append(district)

dist_sorted = sorted(districts, key=lambda k: k['score'])
counter = 0
for x in dist_sorted:
    counter += 1
    #prints as Rank Name Score
    #               Area Perimeter
    print(counter.__str__() + "  " + x['name'].__str__() + " " + x['score'].__str__())
    print("    " + x['area'].__str__() + " " + x['peri'].__str__())

