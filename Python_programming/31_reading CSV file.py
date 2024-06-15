import csv
from datetime import datetime

def reading_CSV():
    with open(r"ww2_warships.csv",'r', newline="") as f:
        s = csv.reader(f, delimiter=",")
        for row in s:
            print(row)


import csv


def year_calc(year):
    now = datetime.now().year
    diff_year = now-int(year)
    return diff_year
def reading_CSV2():
    cleaned_data = []
    with open(r"ww2_warships.csv", 'r', newline="") as f:
        data = csv.DictReader(f, delimiter=",")
        print(data.fieldnames)
        total_weight = 0

        for row in data:
            weight = int(row["weight"].split()[0].replace(",", ""))
            country = row["name"].split(" ")[0]
            name = "".join(row["name"].split(" ")[1:])
            year_built = int(row["date_built"])
            elapsed_year = year_calc(year_built)
            cleaned_data.append({"Country_code": country, "name": name, "weight(ton)": weight ,"year":year_built})
            print(f"{country:5} {name:20} {weight:,} {year_built} {elapsed_year}")
            total_weight += weight

        print(f"total weight {total_weight:,}")

    with open(r"ww2_warships_edited.csv", "w", newline="") as f:
        fieldnames = ["Country_code", "name", "weight(ton)","year"]  # Corrected field name
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        writer.writeheader()
        for row in cleaned_data:
            writer.writerow(row)


# Call the function
reading_CSV2()


