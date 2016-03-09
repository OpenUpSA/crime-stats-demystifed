# Calculating crime numbers per geographical districts by remapping
### Basic stack:
 - Fiona (Python interface to OGR)
 - Shapely (analyzing and manipulating planar geometric objects)
 - Geopandas (heavy lifting of data analysis)
 - gdal command line tools

The geographic information used comes primarily from the Census 2013, SA, data sets. National population data is available at various levels of granularity. Specifically, we used the 2013 Small Area Unit (SAL, 84,907 regions), a unit of area holding from 11 to 11,717 people count (see *data* folder). This is the lowest level unit and the remaining levels are formed by its aggregation (more on why that's desireable below). The population data contains a count of all people in the SAL, split by gender, which can be accessed through a unique SAL identifier. It is those identifiers that bind the SALs to the corresponding area within the Shapefiles.

Crime Statistics consists of the number of 47 classified crimes as reported at each of the 1,142 police stations in a given year.
An interactive map displaying this data at the police precinct level can be explored at the Crime and Justice Hub of the Institute for Security Studies (ISS) site:
https://www.issafrica.org/crimehub/map/

Further, ISS calculated the municipal crime estimates based on the total number of incidents recorded for each police station precinct that have more than 50% of their area fall into the municipality

https://www.issafrica.org/crimehub/municipal/

This crude estimate



```sh
$...
```


### Add-ons and development

Want to contribute? Great!
Contact us at Code for South Africa with your ideas.


License
----

...


**Free Information, open ideas, yeah!**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [open data portal]: <http://data.code4sa.org/>


*see notes/ for details on the SA spatial standards and projections*
