# Calculating crime numbers per geographical districts by means of geo-spatial analysis
Every year SA police reports the numbers of the 47 types of classified crimes as
recorded at the police stations in that given year. However debatable the accuracy of the numbers,
it remains the main official source of the crime data in SA.
This data can be explored e.g. at the Crime and Justice Hub of the Institute for Security Studies
(ISS) site:
https://www.issafrica.org/crimehub/map/

Due to the fact the geographical boundaries of the police districts are not aligned
with any of the official census areas, assessing the corresponding number of crimes at any other geographical level, e.g. municipality or neighborhood, remained an unanswered question.

ISS estimated the levels of municipal crime based on the total number of
corresponding crime incidents recorded for each police station precinct
with more than 50% overlap with a municipality of interest:
 https://www.issafrica.org/crimehub/municipal/

We asked ourselves whether the ISS calculations could be improved,
and more importantly, whether we could design a way of estimating the number of crimes at
a more granular level, e.g. a city or even suburb.
As it turned out, inferring crime statistics at a desired level requires some brainstorming,
bit of maths and coding, yet is far from impossible.

How have we tackled the question?
In brief, we took the geographical boundaries of the police districts, for which the crime
data is available, and the Census boundaries with the population data, overlayed the two
and created smaller intersecting regions, for which both crime and population can be estimated.
Such intersecting areas with all the relevant information can then be aggregated
to form larger area units and can be used to construct a Small Area with a particular location of interest, a neighborhood or a city. The corresponding estimates are just the sums of
the pieces of information we used in the process. Easy.

There are a few things to keep in mind when working with a mix of geo-spatial and numeric data:
- Inherent in this approach is an assumption that the population data is evenly distributed across the census regions. What that in essence means is that whatever region included in the census we decide to look at, there is an equal probability of people living in any part of it. Such assumption will clearly
have less chances to hold if the area is large as the chances of it containing for example
large uninhabited stretches of land (lake, highway) is high. Therefore, we specifically used the lowest level geo-unit for which the population data is available
-- the Small Areas (SAL). In 2013 Census data there were 84,907 SALs, which hold between 11
and 11,717 people count. As mentioned, all other populated areas are formed by
aggregation. Every SAL with its a unique identifier contains a count of all people living in it, split by gender. It is those identifiers that allow us to bind the population data to a geographic area on a map.

- We are comparing geographic areas, calculate ratios, inclusions and slice things up,
and for all of it to make sense we need to make sure that:
  - all the data is in the same coordinate system, and
  - whatever system we work in, the ratio of different areas is maintained, as
   if we were performing the calculations on the surface of the Earth.

   Geographic data was released in a common geo-format, the so-called shapefile,
developed by ESRI and describing spatial vector features. Every shapefile has spatial definition
of its coordinate system. In order to work with both police and population
boundaries and make calculations based on areas (as we do), the data needs to be referenced with respect to a planar surface by means of an equal-area projection. We use the Africa Albers Equal Area Conic (AEA).
See *notes/* for details on the SA spatial standards and projections and *scripts/* for how the data
was processed.


Hereon, we assume that the data is prepped as outlined above and we focus on a particular
type of crime.


The analysis has two steps:

1. First, we estimate the crime rate per person for each of the police precincts.
   As an example, let us choose a precinct P (the analysis is preformed for all).
   The rate estimate becomes: number of crimes in P/number of people in P.
   Thus, in order to calculate the rate, we need an estimate of the total population in P.

   This can be inferred as a sum of people from all intersections of P with SALs:

   - find the SALs that intersect P with intersection area > 0 (no border cases)
   - for each of the intersecting SALs we calculate the number of people that fall in the intersection based on the fraction of SAL's area included in P. For example, if a given SAL with 100 people living
     in it intersects P in 50%, the population of the intersection would be 0.5*100 = 50
    - summing up the populations from such the intersections included in P,
    we get the estimate we are looking for.

2. Given the crime rate per person in P and the population data in all intersections calculated above,
   the expected number of crimes in a SAL is obtained by summing over all its intersections with any of the police precincts and multiplying the number of people
   in a given intersection by the crime rate of the police precinct the intersection belongs to.

To sum up, overlaying the areas of SAL and police precincts results in a set of smaller
regions, which we referred to as intersections, and for which (by making a few assumptions)
we are able to infer number of crimes. Since such intersections make up all the other census
boundaries, we can obtain the crime rates for areas of interest.

Analogous analysis was performed using election boundaries (wards) in place of
Small Areas. With the release of the 2016 re-mapped Ward boundaries (soon!), the data will be
incorporated into the [Wazimap] for easy and dynamic exploration.


### Stack:
 - Fiona (Python interface to OGR)
 - Shapely (analyzing and manipulating planar geometric objects)
 - Geopandas (heavy lifting of data analysis)
 - gdal command line tools
 - pen and paper

### Data
National population data is available at various levels of granularity available
from the SA 2013 Census. The Crime Statistics and Police precincts are available from the [open data portal].
The results sit in the *data* folder.


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
