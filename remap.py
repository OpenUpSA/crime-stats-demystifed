import csv
from collections import defaultdict

headers = "ward_code,Urban_area,Tribal_are,Farm_area,Black_Afri,Coloured,Asian,White,Other_Race,Afrikaans,English,IsiNdebele,IsiXhosa,IsiZulu,Sepedi,Sesotho,Setswana,Sign_Lang,SiSwati,Tshivenda,Xitsonga,Other_Lang,Unspec_Lan,NA_Lang,Primary,Secondary,NTC,Cert_Dip,Tertiary,No_schooli,Other_Edu,A0_9,A10_19,A20_29,A30_39,A40_49,A50_59,A60_69,A70_79,A80Plus".split(",")

weight_reader = csv.DictReader(open("output_remap.csv"))
data_reader = csv.DictReader(open("SAL_Nat_Popn_region-trimmed.csv"))

data = {}
for row in data_reader:
    sal_code = row["SAL_Code_I"]
    data[sal_code] = row

ward_data = defaultdict(lambda: defaultdict(int))
for row in weight_reader:
    ward = row["ward_code"]
    sal = row["sal_code"]
    ward_variables = ward_data[ward]
    ward_variables["ward_code"] = ward

    for variable in headers[1:]:
        sal_data = int(data[sal][variable])  # e.g. Black Africans
        sal_weight = float(row["weight"])  # e.g. 0.5
        data_allocation = sal_data * sal_weight  # e.g 50% of 100 Black Africans = 50

        ward_variables[variable] += data_allocation

with open("remapped_data.csv", "w") as fp:
    writer = csv.DictWriter(fp, headers)
    writer.writeheader()
    for value in ward_data.values():
        writer.writerow(value)
