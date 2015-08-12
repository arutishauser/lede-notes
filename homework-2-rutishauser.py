#Arthur Rutishauser
#06, 01, 2015
#Homework 2

print "Lists"

print "Question 0"

liste = [22, 90, 0, -10, 3, 22, 48]
print liste

print "Question 1"
print len(liste)

print "Question 2"
print liste [3]

print "Question 3"
print liste [1] + liste [3]

print "Question 4"
print sorted(liste)[-2]

print "Question 5"
print liste[-1]

print "Question 6"
for number in liste:
	if number < 10:
		print number, number * 30
		if number % 2 != 0:
			print number, number * 30 + 6

for number in liste:
	if number > 50:
		print number, number - 10


for number in liste:
	if number != -10:
		print number, number - 1


for number in liste:
	print number, number / 2

print "Question 7"
print sum(liste)/2.0

print "Dictionaries"

print "Question 8"
movieo = {'title': "Casablanca", 'year': 1942, 'director': "Michael Curtiz"}
print "My favorite movie is", movieo['title'], "which was released in", movieo['year'], "and was directed by", movieo['director']

print "Question 9"
movie = {'title': "Casablanca", 'year': 1942, 'director': "Michael Curtiz"}
movie ["Budget"] = 878000
movie ["revenue"] = 3700000
print "The old Dictionnary", movieo, "shows neither Budget nor Revenue like the new Dictionnary"
print movie

print "Question 10"
print movie["revenue"] - movie["Budget"], "Dollars"
if ["Budget"] > ["revenue"]:
	print "It was a flop"
else:
	print "That was a good investment"

print "Question 11"
newyork = {
"Manhattan": 1.6,
"Brooklyn": 2.6, 
"Bronx": 1.4, 
"Queens": 2.3, 
"Staten Island": 0.47}
print newyork

print "Question 12"
print "Brooklyn has ", newyork ["Brooklyn"], "million residents"

print "Question 13"
print sum(newyork.values()), "millions live in all five boroughs"

print "Question 14"
print "%.2f" %(newyork ["Manhattan"]/sum(newyork.values())*100)


print "Question 15"
from pprint import pprint
pprint(newyork)
newyork = {
"Manhattan": 1.6,
"Brooklyn": 2.6, 
"Bronx": 1.4, 
"Queens": 2.3, 
"Staten Island": 0.47}

print "Question 16"

print {k:v for (k,v) in newyork.items() if v > 1}

millionenteile = {k:v for (k,v) in newyork.items() if v > 1}
print millionenteile.items()

print "These boroughs of New York have more than one million inhabitants:"
for k, v in millionenteile.items():
	print k, "with", v, "million inhabitants"

print "Question 17"
print len(millionenteile), "boroughs of New York have more than one million inhabitants"


print "Question 18"
alphabet = newyork.keys()
alphabet_sort = sorted(alphabet)
print alphabet_sort[0], "is the borough with the name that comes first in the alphabet.", "It has", len(alphabet_sort[0]), "characters." 

print "Extra"
print newyork ["Staten Island"]
print len(newyork.keys())
print len("Staten Island")

lengths = [len(k) for k in newyork.keys()]
print lengths
lengths_sort = sorted(lengths)
print lengths_sort
print "Staten Island is the longest with", lengths_sort[-1]

print newyork.keys(), newyork.values()
print newyork

print "Question 19"
for k, v in newyork.items():
	print k, "has", v, "million inhabitants"

print "other possibility:"
print("\n".join("{}: {} millions".format(k, v) for k, v in newyork.items()))




