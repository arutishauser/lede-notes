import dateutil.parser
# or import parser from dateutil
import datetime
import csv
import urllib2
import os

# 1 cup = 16 tablespoons
def to_cups(amount, unit):
	if unit == "tablespoons":
		return float(amount/16.0), "cups"
	if unit == "teaspoons":
		return float(amount/48.0), "cups"
	elif unit == "cups":
		return amount, unit

print to_cups(3, 'tablespoons')


def to_tablespoons(amount, unit):
 	if unit == "teaspoons":
		return float(amount/3.0)
	if unit == "cups":
		return float(amount/0.0625)
	elif unit == "tablespoons":
		return amount, unit
print to_tablespoons(0.25, 'cups')


def to_teaspoons(amount, unit):
	if unit == "tablespoons":
		return float(amount)*3
	if unit == "cups":
		return float(amount/0.0208333)
	elif unit == "teaspoons":
		return amount, unit
print to_teaspoons(1, 'cups')


dry_ingredients = ["salt", "flour", "baking powder", "baking soda", "cinnamon", "yeast"]
wet_ingredients = ["water", "butter", "egg", "milk", "chocolate", "sugar"]

def to_grams(amount, measurement, ingredient):
	if ingredient in dry_ingredients:
		if measurement == "cups":
			return float(amount) * 125 
		# 7.8 grams in a tablesoon of flour
		elif measurement == "tablespoons":
			return float(amount) * 7.8
		# 1 teaspoon of flour is 2.6 grams
		else:
			return float(amount) * 2.6
	elif ingredient in wet_ingredients:
		if measurement == "cups":
			return float(amount) * 240
		# one tablespoon of sugar is 12 grams
		elif measurement == "tablespoons":
			return float(amount) * 12
		# one teaspoon of sugar is 4 grams
		else:
			return float(amount) * 4
	else:
		return "I have no idea"
print to_grams(11.5, "teaspoons", "yeast")
#print dry_ingredients

recipe = [
  { 'amount': 3, 'measurement': 'cups', 'ingredient': 'flour' },
  { 'amount': 1, 'measurement': 'tablespoons', 'ingredient': 'milk' },
  { 'amount': 0.25, 'measurement': 'teaspoons', 'ingredient': 'salt' },
  { 'amount': 1, 'measurement': 'cups', 'ingredient': 'butter' },
  { 'amount': 0.75, 'measurement': 'cups', 'ingredient': 'baking powder' },
  { 'amount': 0.25, 'measurement': 'cups', 'ingredient': 'egg' }
]

weights = []
for line in recipe:
	weights.append(to_grams(line['amount'], line['measurement'], line['ingredient']))

print sum(weights)



def grams_to_measurement(amount, ingredient, measurement):
	conversion = to_grams(1, measurement, ingredient)
	inverse = 1/conversion
	return inverse * amount

print grams_to_measurement(300, "flour", "cups"), "grams_to_measurement"

def baker_percentage(amount, measurement, ingredient):
	flour_in_grams = to_grams(amount, measurement, ingredient)
	water_in_grams = flour_in_grams * 0.35
	milk_in_grams = flour_in_grams * 0.35
	yeast_in_grams = flour_in_grams * 0.04
	salt_in_grams = flour_in_grams * 0.018
	return "cups of flour:", grams_to_measurement(flour_in_grams, "flour", "cups"), "cups of water:", grams_to_measurement(water_in_grams, "water", "cups"), "cups of milk:", grams_to_measurement(milk_in_grams, "milk", "cups"), "teaspoons of yeast:", grams_to_measurement(yeast_in_grams, "yeast", "teaspoons"), "teaspoons of salt:", grams_to_measurement(salt_in_grams, "salt", "teaspoons")

print baker_percentage(6, "cups", "flour")

