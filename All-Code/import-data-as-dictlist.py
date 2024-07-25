import csv

f = open('../fulldataset.csv', 'r')

reader = csv.DictReader(f)

poems = list(reader)

print("The list of dictionaries is: ")
print(poems)
