#Arthur Rutishauser
#06, 11, 2015
#Homework 4

import csv
file = open('dogs.csv')
#dogs = csv.reader(file) geht nicht gut
#das file umwandeln in eine Liste
dogs = list(csv.DictReader(file))


print "Homework 4 Question 1"

dog_names = []
for dog in dogs:
	if dog['dog_name'] not in dog_names:
		dog_names.append(dog['dog_name'])


dog_namess=dog_names

dog_name_counts = {}
for dog_name in dog_namess:
	dog_name_counts[dog_name] = 0
for dog in dogs:
	dog_name = dog['dog_name']
	dog_name_counts[dog_name] = dog_name_counts[dog_name] + 1
print dog_name_counts

print "Question 2"
print dog_name_counts ['Danger'], "dogs are named Danger"

print "Question 3"
x= float(dog_name_counts ['Danger'])
y= float(dog_name_counts ['Spike'])
z=float(x/y)
ratio = int(1/z)
print "The name Spike appears", ratio, "times more than Danger"

print "Question 4"

millionenteile = {k:v for (k,v) in dog_name_counts.items() if v == 1}
print millionenteile.items()
xmillionenteile=millionenteile.items()

xmillionenteile_sort = sorted(xmillionenteile, key=lambda x:x [0])
print xmillionenteile_sort, "these dogs are only once named"
millionenteile_sort = sorted(millionenteile, key=str.lower)
print millionenteile_sort, "these dogs are only once named and sorted with key=str.lower. how is it possible to combine the keys?"


print "Question 5"



boroughs = []
for dog in dogs:
	if dog['borough'] not in boroughs:
		boroughs.append(dog['borough'])


boroughss=boroughs

borough_counts = {}
for borough in boroughss:
	borough_counts[borough] = 0
for dog in dogs:
	borough = dog['borough']
	borough_counts[borough] = borough_counts[borough] + 1
print borough_counts, "these are the dogs"

population = {'Staten Island': 468000, 'Brooklyn': 2504000, 'Bronx': 1385000, 'Manhattan': 1585000, 'Queens': 2231000}
print population, "these are the populations"


class MyDict(dict):
    def __div__(self, oth):
        r = self.copy()

        try:
            for key, val in oth.items():
                if key in r:
                    r[key] /= int(val) # You can custom it here
                else:
                    r[key] = val
        except AttributeError: # In case oth isn't a dict
            return NotImplemented # The convention when a case isn't handled

        return r

c = MyDict(population)
d = MyDict(borough_counts)

merger = (c/d)


from collections import OrderedDict
d_sorted_bymerger = OrderedDict(sorted(merger.items(), key=lambda x: x[0]))
print "this shows the ratio of dogs to people", ("\n".join("{}: {} dogs".format(k, v) for k, v in d_sorted_bymerger.items())), " \n Staten Island and so the lowest ratio ans so they love dogs the best "

print "Question 6"

count_zip_code = []
for dog in dogs:
	
	if dog['zip_code'] not in count_zip_code:

		count_zip_code.append(dog['zip_code'])




count_zip_codesa = []
for dog in dogs:
	count_zip_codesa.append(dog['zip_code'])

from collections import Counter
mczip_code= [ite for ite, it in Counter(count_zip_codesa).most_common(1)]



czip_code = {}

for i in count_zip_codesa: czip_code[i] = czip_code.get(i, 0) + 1

counters = ("\n".join("{}: {} dogs".format(k, v) for k, v in czip_code.items()))

czip_codeteile = {k:v for (k,v) in czip_code.items() if int(k) <= 10128}


from collections import OrderedDict
d_sorted_by_zip_codevalue = OrderedDict(sorted(czip_codeteile.items(), key=lambda x: x[0]))
print ("\n".join("{}: {} dogs".format(k, v) for k, v in d_sorted_by_zip_codevalue.items()))

print "you see that in the Lower Eastside for every Zipcode region (10002, 10003, 10009)ther are 774, 1000, 1065 dogs registred, \n but in the Upper eastside ther are in two zip code regions (10065, 10075), 0 dogs registred, in one (10044) 79. "




