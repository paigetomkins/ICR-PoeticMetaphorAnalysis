import csv

f = open('/home/paige-tomkins/ICR-linguistics/all.csv', 'r')

reader = csv.DictReader(f)

poems = list(reader)

#for dictionary in reader:
 #   poems.append(dictionary)
print("The list of dictionaries is: ")
print(poems)
