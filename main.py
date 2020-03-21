import csv

# Importing package data from packages_data.csv
with open('data/packages_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file)

    for row in csv_reader:
        print(row)