

def double(number):
	bigger = number*2
	#return 7 wuerde stoeren, man kann nur einmal zurueckgeben
	return bigger

print double(3)

#double =40
number = 40
print double(number)

def exclaim(sentence):
	return sentence + "!!!!!!"+"jlkhh"

print exclaim("was auch immer")

#nicht funktioniert print exclaim("was auch immer", "was noch")

print round(3.49657654, 4)

#if boat_count > car_count:
#	print "Larger"
#else:
#	print "smaller"

#if motorcycle_count > car_count:
#	print "Larger"
#else:
#	print "smaller"


def size_comparison(countA, countB):
	if countA > countB:
		return "Larger"
	else:
		return "Smaller"



result = size_comparison(34, 56)

print result
