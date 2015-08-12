#Arthur Rutishauser
#06, 06, 2015
#Homework 2

import csv
file = open('sample.csv')
#dogs = csv.reader(file) geht nicht gut
#das file umwandeln in eine Liste
dogs = list(csv.DictReader(file))

print "Question 1"
count_dogsa = []
for dog in dogs:
	count_dogsa.append(dog['dog_name'])
print count_dogsa
# Frage 1
print len(count_dogs)

for dog in dogs:
	print dog ['borough']


print "Question 2"

Manhattan = "Manhattan"
Manhattan = 0
for dog in dogs:
	if dog['borough'] == "Manhattan":
		Manhattan = Manhattan + 1
print Manhattan, "dogs are registrated in Manhattan."

Bronx = "Bronx"
Bronx = 0
for dog in dogs:
	if dog['borough'] == "Bronx":
		Bronx = Bronx + 1
print Bronx, "dogs are registrated in the Bronx."


Queens = "Queens"
Queens = 0
for dog in dogs:
	if dog['borough'] == "Queens":
		Queens = Queens + 1
print Queens, "dogs are registrated in Queens."

Brooklyn = "Brooklyn"
Brooklyn = 0
for dog in dogs:
	if dog['borough'] == "Brooklyn":
		Brooklyn = Brooklyn + 1
print Brooklyn, "dogs are registrated in Brooklyn."

Staten_Island = "Staten Island"
Staten_Island = 0
for dog in dogs:
	if dog['borough'] == "Staten Island":
		Staten_Island = Staten_Island + 1
print Staten_Island, "dogs are registrated in Staten Island."