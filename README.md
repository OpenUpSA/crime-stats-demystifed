# Calculating crime numbers per geographical districts by means of geo-spatial analysis
Every year SA police reports the numbers of the 47 types of classified crimes as
recorded at the police stations in a given year. However debatable the accuracy of the numbers,
this is the main official source of the crime data in SA.

An interactive map allowing for exploration of this data can be
found at the Crime and Justice Hub of the Institute for Security Studies
(ISS) site:
https://www.issafrica.org/crimehub/map/

The number of crimes at any other geographical level though, e.g. municipality or neighborhood,
has been an unanswered question.
This is due to the fact the geographical boundaries of the police districts are not aligned
with the official census areas, thus to infer the crime statistics at a desired level
 takes a bit more than basic calculus. Still, it is not impossible.

ISS estimated the levels of municipal crime based on the total number of
corresponding crime incidents recorded for each police station precinct
with more than 50% overlap with a municipality of interest:
 https://www.issafrica.org/crimehub/municipal/

We asked ourselves whether the ISS calculations could be improved,
and more importantly, whether we could design a way of estimating the number of crimes at
a more granular level, e.g. a city or even suburb.

In brief, we took the geographical boundaries of the police districts, for which the crime
data is available, and the Census boundaries with the population data, overlayed the two
and created smaller intersecting regions, for which both crime and population can be estimated.
Such intersecting areas with all the relevant information can then be aggregated
to form larger area units and can be used to construct a Small Area with a particular location of interest, a neighborhood or a city. The corresponding estimates are just the sums of
the pieces of information we used in the process. Easy.

There are a few things to keep in mind:
- Inherent in this approach is an assumption that the population data is evenly distributed across the census regions. What that in essence means is that whatever region included in the census we decide to look at, there is an equal probability of people living in any part of it. Such assumption will clearly
have less chances to hold if the area is large as the chances of it containing for example
large uninhabited stretches of land (lake, highway) is high. Therefore, we specifically used the lowest level geo-unit for which the population data is available
-- the Small Areas (SAL). In 2013 Census data there were 84,907 SALs, which hold between 11
and 11,717 people count. As mentioned, all other populated areas are formed by
aggregation. Every SAL with its a unique identifier contains a count of all people living in it, split by gender. It is those identifiers that allow us to bind the population data to a geographic area on a map.

- We are comparing geographic areas, calculate ratios, inclusions and slice things up,
and for all of it to make sense we need to make sure that:
   1. all data is in the same coordinate system, and
   2. whatever system we work in, the ratio of different areas is maintained, as
   if we would perform the calculations on the surface of the Earth.

   Geographic data was released in a common geo-format, the so-called shapefile,
developed by ESRI and describing spatial vector features. Every shapefile has spatial definition
of its coordinate system. In order to work with both police and population
boundaries and make calculations based on areas (as we do), the data needs to be referenced with respect to a planar surface by means of an equal-area projection. We use the Africa Albers Equal Area Conic (AEA).
See *notes/* for details on the SA spatial standards and projections and *scripts/* for how the data
was processed.


Finally, the maths of it.
For each police precinct,




### Stack:
 - Fiona (Python interface to OGR)
 - Shapely (analyzing and manipulating planar geometric objects)
 - Geopandas (heavy lifting of data analysis)
 - gdal command line tools
 - pen and paper



```sh
$...
```
### Data
National population data is available at various levels of granularity available
from the SA 2013 Census. The Crime Statistics and Police precincts are available from the [open data portal].
The results sit in the *data* folder.

## What happens next
With the release of the 2016 re-mapped Ward boundaries (soon!), the data will be
incorporated into the [Wazimap] for easy and dynamic exploration.


### Add-ons and development

Want to contribute? Have an idea for improvement? Great!
Get in touch.

License
----

...


**Knowledge is power, yeah!**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [open data portal]: <http://data.code4sa.org/>
   [Wazimap]: <http://wazimap.co.za/>
