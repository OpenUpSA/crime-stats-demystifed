import sys
from shapely.geometry import shape
from shapely.geos import TopologicalError
from fiona import collection
import rtree

LAYER1 = "data/sal.shp"
LAYER1_KEY = "sal_code_i"
LAYER2 = "/Users/greg/coding/SA-Maps/Wards/Wards2011.shp"
LAYER2_KEY = "WARD_ID"

with open("output_remap.csv", "w") as fp:
    layer1 = collection(LAYER1, "r")
    layer2 = collection(LAYER2, "r")

    fp.write("sal_code,ward_code,weight\n")
    index = rtree.index.Index()
    sys.stderr.write("Creating index over %d items\n" % len(layer1))

    for feat1 in layer1:
        fid = int(feat1['id'])
        geom1 = shape(feat1['geometry'])
        index.insert(fid, geom1.bounds)
        sys.stderr.write(".")
    sys.stderr.write("Index created")

    for feat2 in layer2:
        geom2 = shape(feat2['geometry'])
        for fid in list(index.intersection(geom2.bounds)):
            feat1 = layer1[fid]
            geom1 = shape(feat1['geometry'])
            try:
                intersection = geom1.intersection(geom2)
                if intersection.area > 0:
                    feat1_key = int(feat1["properties"][LAYER1_KEY])
                    feat2_key = int(feat2["properties"][LAYER2_KEY])
                    fp.write("%s,%s,%s\n" % (feat1_key, feat2_key, intersection.area / geom1.area))
            except TopologicalError, e:
                print e
