import sys
import os
from shapely.geometry import shape
from shapely.geos import TopologicalError
from fiona import collection
import rtree
import csv

LAYER1 = "data/sal.shp"
LAYER1_KEY = "sal_code_i"
LAYER2 = "data/Police_bounds.shp"
LAYER2_KEY = "COMPNT_NM"

# read in populations
reader = csv.DictReader(open("data/sal_population.csv"))
pop1 = {row["small_area"]: float(row['population']) for row in reader}

reader = csv.DictReader(open("data/precinct_population.csv"))
pop2 = {row["precinct"]: float(row['population']) for row in reader}


with open("precinct_to_sal_weights.csv", "w") as fp:
    layer1 = collection(LAYER1, "r")
    layer2 = collection(LAYER2, "r")

    fp.write("small_area,precinct,weight\n")

    if os.path.exists('sal.idx'):
        index = rtree.index.Index('sal')
        print "Using existing index"
    else:
        index = rtree.index.Index('sal')
        print "Creating index over %d items\n" % len(layer1)

        for feat1 in layer1:
            fid = int(feat1['id'])
            geom1 = shape(feat1['geometry'])
            index.insert(fid, geom1.bounds)
        print "Index created"

    sys.stderr.write("Intersecting over %d items\n" % len(layer2))
    for feat2 in layer2:
        geom2 = shape(feat2['geometry'])

        for fid in list(index.intersection(geom2.bounds)):
            feat1 = layer1[fid]
            geom1 = shape(feat1['geometry'])

            try:
                intersection = geom1.intersection(geom2)
                if intersection.area > 0:
                    feat1_key = int(feat1["properties"][LAYER1_KEY])
                    feat2_key = feat2["properties"][LAYER2_KEY]

                    weight = intersection.area / geom1.area * pop1[str(feat1_key)] / pop2[feat2_key]
                    fp.write("%s,%s,%s\n" % (feat1_key, feat2_key, weight))

            except TopologicalError, e:
                print e
