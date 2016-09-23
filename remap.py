import csv
from collections import defaultdict

weight_reader = csv.DictReader(open("sal_to_precinct_weights.csv"))
data_reader = csv.DictReader(open("data/sal_population.csv"))

SOURCE_KEY = "small_area"
TARGET_KEY = "precinct"

source_data = {}
for row in data_reader:
    sal_code = row["small_area"]
    source_data[sal_code] = row

headers = source_data.values()[0].keys()
headers.remove(SOURCE_KEY)

final_data = defaultdict(lambda: defaultdict(int))
for row in weight_reader:
    target_code = row[TARGET_KEY]
    source_code = row[SOURCE_KEY]
    row_data = final_data[target_code]
    row_data[TARGET_KEY] = target_code

    for variable in headers:
        sal_data = int(source_data[source_code][variable])  # e.g. Black Africans
        sal_weight = float(row["weight"])  # e.g. 0.5
        data_allocation = sal_data * sal_weight  # e.g 50% of 100 Black Africans = 50

        row_data[variable] += data_allocation

with open("remapped_data.csv", "w") as fp:
    writer = csv.DictWriter(fp, final_data.values()[0].keys())
    writer.writeheader()
    for value in final_data.values():
        writer.writerow(value)
