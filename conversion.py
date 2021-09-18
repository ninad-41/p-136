import csv

finaldict = {}

with open('star_with_gravity.csv', mode = 'r') as f:
    reader = csv.reader(f)
    dict_from_csv = {rows[0]:rows[1] for rows in reader}
print(dict_from_csv)