# General intro for SA cartographic/geo- systems

Shapes and information displayed on maps are a result of transforming the measurements
performed on Earth's surface through a composition of functions:
choice,representation of a spheroid (datum) + projection on geographic/geodesic/planar coordinates.
Depending on the location of the analysis and it purpose, the definitions of the above.

##DATUM
There are two principal datums used in South Africa:

1. Cape (obsolete)
2. Hartebeesthoek94 (current).

The Cape datum is the older of the two and no longer in use. It references
the Clarke 1880 ellipsoid and was developed by Sir Thomas Maclear and
Sir David Gill in the late 19th - early 20th Century with its orgin
at Buffelsfontein, Port Elizabeth.

Since 01/01/1999 the official coordinate system for South Africa
is the Hartebeesthoek94 geodetic datum: based on the World Geodetic System 1984 ellipsoid,
commonly known as WGS84, with the International Terrestrial Reference Frame
1991 coordinates of the Hartebeesthoek Radio Astronomy Observatory Telescope
(west of Johannesburg near the Cradle of Humankind) used as the origin of this system.

##PROJECTIONS
Default/optimal projections in SA use the Transverse Mercator
Projection referred to as e.g. "Hartebeesthoek94 Lo15", where the "Lo15" indicates
the zone name (named after the value of its origin, similarly to UTM Zones).

It is a variation of the UTM projection that defines the national coordinate system
in SA called “Gauss Conformal Projection” (form of Gauss–Krüger, EPSG projection 2047).
It is used for the computation of the plane YLo and XLo co-ordinates, commonly known as the "Lo. co-ordinate system".
The equator will project as a straight line, at right angles to the central meridian (Lo.),
but all other meridians and parallels will project as curved lines.
The principles of the projection are the same as the UTM with a difference that
each zone is only 2° wide (as opposed to 6° in the standard UM, this less distortion
and no scale factor).
Only the area within one degree of longitude on either side of the central
meridian is projected. The width of each segment (belt) is thus two degrees
of longitude and is referred to the central meridian (CM) of that belt.

- X (Southings) coordinates are measured southwards from the equator,
increasing from the equator (where X = 0m) towards the South Pole.
- Y (Westings) coordinates are measured from the CM of the respective zone,
increasing from the CM (where Y=0) in a westerly direction.

Longitudes 17°East, 19°East, 21°East, 23°East, 25°East, 27°East, 29°East,
31°East and 33°East are used as the mid-points of each 2° projection.
These coordinate zones were Lo17, Lo19, Lo21 etc in Cape Datum
(until 1999) and are now referred to as Wg17, Wg19, Wg21 etc
(Haartebeeshoek 1994 datum).

E.g.
The coordinate zone in use in the Durban area is Wg31 as the longitude 31°
east runs directly through the city. Cape Town is Wg17-Wg18.


## PROCESS:
###General things to note:
1. It is good practice to store a version of the data in the projection
in which it was captured. Re-projection can be a lossy process,
and it is important to have the original data, e.g. storing in WGS84 for the sake of
simplicity. For overlaying vector in google maps this will be enough.

2. For the calculations we need to re-project in meters (planar projection)

3. There is a number of important mutually exclusive classes of projections,
each having distinctive geometric qualities and used for different purposes:

- Conformal (or orthomorphic) projections preserve angular relationships between
great circles (=preserving shapes). They do not maintain correct areal scales.

- Equal area (or equivalent/equiareal/authalic) projections preserve areal relationships.
In other words, given any two regions A and B on the Earth and the corresponding
regions A' and B' on an equal-area map, the surface ratios A/A' and B/B' are
identical (A and B need not have the same shape; shapes A and A' will probably be different).
An equal-area projection is not necessarily equidistant; in fact, in order to preserve area,
at any point the scale distortion in a given direction must be the inverse
of the scale distortion in the orthogonal direction. For instance, along the
Equator in the conventional aspect of Mollweide's projection the horizontal
scaling factor is slightly less than 1, and slightly above 1 in the vertical direction;
the net effect is making the continents a bit too slender.


## Africa datums/projections
- esri.extra.pin:102011
Africa Sinusoidal
proj=sinu
lon_0=0
x_0=0
y_0=0
ellps=WGS84
datum=WGS84
units=m
no_defs

-esri.extra.pin:102022
Africa Albers Equal Area Conic
proj=aea
lat_1=20
lat_2=-23
lat_0=0
lon_0=25
x_0=0
y_0=0
ellps=WGS84
datum=WGS84
units=m
no_defs

-esri.extra.pin:102023
Africa Equidistant Conic
proj=eqdc
lat_0=0
lon_0=0
lat_1=20
lat_2=-23
x_0=0
y_0=0
ellps=WGS84
datum=WGS84
units=m
no_defs

-esri.extra.pin:102024
Africa Lambert Conformal Conic
proj=lcc
lat_1=20
lat_2=-23
lat_0=0
lon_0=25
x_0=0
y_0=0
ellps=WGS84
datum=WGS84
units=m
no_defs

-esri.pin:102011
Africa Sinusoidal
proj=sinu
lon_0=0
x_0=0
y_0=0
ellps=WGS84
datum=WGS84
units=m
no_defs

-esri.pin:102022
Africa Albers Equal Area Conic
proj=aea
lat_1=20
lat_2=-23
lat_0=0
lon_0=25
x_0=0
y_0=0
ellps=WGS84
datum=WGS84
units=m
no_defs

-esri.pin:102023
Africa Equidistant Conic
proj=eqdc
lat_0=0
lon_0=0
lat_1=20
lat_2=-23
x_0=0
y_0=0
ellps=WGS84
datum=WGS84
units=m
no_defs

-esri.pin:102024
Africa Lambert Conformal Conic
proj=lcc
lat_1=20
lat_2=-23
lat_0=0
lon_0=25
x_0=0
y_0=0
ellps=WGS84
datum=WGS84
units=m
no_defs

-world.pin:nw-africa
Northwest Africa
proj=lcc
ellps=clrk80
lat_1=34dN
lon_0=0dE
x_0=1000000
y_0=500000
k_0=0.99908
no_defs

## Calculations based on shapefiles

Using estimators based on geographic areas requires equal area projection
on a planar surface. Out choice is Africa Albers Equal Area Conic (AEA).

Census boundaries are defined as non-Earth (?) EPSG:4148. As a matter of fact,
the 2013 thapefiles were distributed without the projection (.prj) file, which albeit contrary
to the logic behind releasing data to the public, happens surprisingly often.
It is a safe assumption to make that the projection used in 2013 follow the 2011
format, as well as the standards of the other data that come from the same source/data provider.
We therefore copied the .prj file from one of the Census shapefiles of 2011 (SP=subplace).

In principle, EPSG: 4148 is the same as EPSG:4236  (unless modified for specific purposes).
To be on a safe side though and avoid mislabelling, we re-projected the data explicitly.
Police Precinct shapefiles are already in EPSG:4236.

*Note:*
EPSG 4326 (WGS84):  +proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs

EPSG 4148 (Hartebeesthoek94): +proj=longlat +ellps=WGS84 +towgs84=0,0,0,0,0,0,0 +no_defs

Next, we used AEA to project the data on a planar surface maintaing the relative areas.

## Resources, info, tools, Python:

####A list of coordinate systems for South Africa (useful for changing coordinates):
- http://epsg.io/?q=south%20africa
- http://spatialreference.org/ref/epsg/2047/

####Other useful ref links:
- http://www.spatialreference.co.za/Maps.asp

####Quick projection & EPSG code finders:
- http://projfinder.com/
- http://www.prj2epsg.org/epsg/4326

####SA boundaries:
- http://geoportal.rcmrd.org/layers/?limit=100&offset=0&regions__name__in=South%20Africa
e.g. provinces:
http://geoportal.rcmrd.org/layers/servir%3Asouth_africa_adm2

####Definition of projection parameters for Python proj (PROJ4 wrapper):
http://proj.maptools.org/gen_parms.html
- Coordinate Reference System (CRS) of the data is stored in the .crs property
(use Pyepsg)
