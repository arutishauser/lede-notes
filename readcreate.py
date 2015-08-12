import csv
file = open('output1.csv')
#dogs = csv.reader(file) geht nicht gut
#das file umwandeln in eine Liste
output = list(csv.DictReader(file))
print output