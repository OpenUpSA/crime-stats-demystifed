#!/bin/bash


# ogr2ogr reprojects vector data
# Remove SP_CODE in SAL- too long? problems saving the field when re-projecting

# SAL is in 4148 and needs to be projected twice: onto 4326 and then on a plane using Africa Equal Area Albers Conic
ogr2ogr -f "ESRI Shapefile" shapefiles/updated/sal_population_4326.shp -t_srs EPSG:4326 -s_srs EPSG:4148 shapefiles/updated/sal_population/sal_population.shp
ogr2ogr -t_srs '+proj=aea +lat_1=20 +lat_2=-23 +lat_0=0 +lon_0=25 +x_0=0 +y_0=0 +ellps=WGS84 +datum=WGS84 +units=m +no_defs' shapefiles/updated/sal_population_aea.shp shapefiles/updated/sal_population_4326.shp

# police precincts only on the surface
ogr2ogr -s_srs EPSG:4326 -t_srs '+proj=aea +lat_1=20 +lat_2=-23 +lat_0=0 +lon_0=25 +x_0=0 +y_0=0 +ellps=WGS84 +datum=WGS84 +units=m +no_defs' shapefiles/updated/polPrec_murd2015_prov_aea.shp shapefiles/updated/polPrec_murd2015_prov/polPrec_murd2015_prov.shp

#wards 2011
ogr2ogr -s_srs EPSG:4326 -t_srs '+proj=aea +lat_1=20 +lat_2=-23 +lat_0=0 +lon_0=25 +x_0=0 +y_0=0 +ellps=WGS84 +datum=WGS84 +units=m +no_defs' Wards2011_aea.shp Wards2011.shp
