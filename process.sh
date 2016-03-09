#!/bin/bash

sed -i -e 1,6d data/sal_population.csv
cat data/sal_population.csv | sed 's/"//g' | awk '{FS="\,"; s = $2+$3; print $1","s }' \
                > data/sal_processed_temp.csv

# add a header
echo "district, count" > header_sal.txt
cat header_sal.txt data/sal_processed_temp.csv > data/sal_processed.csv

# 2014 data:
#cat Police_Statistics.csv | grep Murder | grep 2014 > pstat_murder_2014.csv

# 2015 data
cat data/Police_Statistics_2015_location.csv | cut -d',' -f5,7,17,21 | grep Murder \
      > data/crime_murd_temp.csv

echo "PoliceStation,Crime,Incidents,Province" > header2015.txt
cat header2015.txt data/crime_murd_temp.csv > data/pp_murder_2015.csv

rm data/crime_murd_temp.csv

rm header*txt

# adding all types of crimes:
cat Police_Statistics_2015_location.csv | cut -d',' -f7 | sort -u | sed 's/17 //g'  > types_crimes.txt

# making a header:
cat Police_Statistics_2015_location.csv | cut -d',' -f7 | sort -u | sed 's/17 //g' | sed 's/ /_/g' | tr '\n' '\t'
# all crimes:
cat Police_Statistics_2015_location.csv | cut -d',' -f5,7,17,21 > pp_crime_2015_nh.csv

cat header2015.txt pp_crime_2015_nh.csv > pp_crime_2015.csv
