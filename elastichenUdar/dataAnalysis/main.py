import csv

with open("elastichenUdar.csv", newline='') as file:
    reader = csv.reader(file, delimiter=' ', quotechar='|')
    for row in reader:
        print(row)
