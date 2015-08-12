#Arthur Rutishauser
#05, 27, 2015
#Homework 1
print "enter your name: ",
name = raw_input()

print "Hello", name

year_of_birth = raw_input("Enter your year of birth:")

if int(year_of_birth) > 2015:
	print "do it again"
	year_of_birth = raw_input("Enter your year of birth:")


age = 2015 - int(year_of_birth)
print name, "You are approximately", age, "years old"

heartbeats = 35 * age
print name, "Your heart has beaten approximately", heartbeats, "million times"

whale = heartbeats / 8
print name, "If your were a blue whale, your heart would have beaten approximately", whale, "million times"

rabbit = 132.0/72.0 * heartbeats
rabbitm = 325.0 / 72.0 * heartbeats
print name, "If your were a rabbit, your heart would have beaten from ", int(rabbit), "up to", int(rabbitm), "million times"

brabbit = rabbit/1000.0
brabbitm = rabbitm/1000.0

if rabbit > 1000:
	print "This would be between ", ("%.2f" %  brabbit)

if rabbit <= 1000:
	print "This would be between ", int(rabbit), "millions"

if rabbitm > 1000:
	print "and", ("%.2f" %  brabbitm), "Billion times"

if rabbitm <= 1000:
	print "and", int(rabbitm), "Million times"


venus = age * 365.00/224.68
print "Your age is about", int(venus), "venus years"

neptun = age / 164.81
print "Your age is about", ("%.2f" % neptun), "neptun years"

altersdifferenz= 1965 - int(year_of_birth)
jungerdifferenz= int(year_of_birth) - 1965

if (int(year_of_birth) % 2) == 0:
   print("Hooray you are borne in a even year")
else:
   print("Hooray you are borne in a odd year")


if int(year_of_birth)/2 == int:
	print "Hooray you are borne in a even year"
else:
	print "Hooray you are borne in a odd year"

if int(year_of_birth) == 1965:
	print "Hooray, you have the same age"

if int(year_of_birth) < 1965:
	print "you are", altersdifferenz, " years older"

if int(year_of_birth) > 1965:
	print "you are", jungerdifferenz, " years younger"


if int(year_of_birth) <= 1974 and int(year_of_birth) < 1975:
	print "Pittsburg won 6 times the Super Bowl since you are borne"

if int(year_of_birth) >= 1975 and int(year_of_birth) < 1978:
	print "Pittsburg won 5 times the Super Bowl since you are borne"

if int(year_of_birth) >= 1974 and int(year_of_birth) < 1979:
	print "Pittsburg won 4 times the Super Bowl since you are borne"

if int(year_of_birth) >= 1979 and int(year_of_birth) < 2005:
	print "Pittsburg won 3 times the Super Bowl since you are borne"

if int(year_of_birth) >= 2005 and int(year_of_birth) < 2008:
	print "Pittsburg won 2 times the Super Bowl since you are borne"

if int(year_of_birth) == 2008:
	print "Pittsburg won 1 times the Super Bowl since you are borne"
if int(year_of_birth) > 2008:
	print "Pittsburg won never times the Super Bowl since you are borne"


if int(year_of_birth) >= 1933 and int(year_of_birth) < 1945:
	print "Franklin D. Roosevelt was President when you were born"

if int(year_of_birth) >= 1945 and int(year_of_birth) < 1953:
	print "Harry S. Truman was President when you were born"

if int(year_of_birth) >= 1953 and int(year_of_birth) < 1961:
	print "Dwight D. Eisenhower was President when you were born"

if int(year_of_birth) >= 1961 and int(year_of_birth) < 1964:
	print "John F. Kennedy was President when you were born"

if int(year_of_birth) >= 1964 and int(year_of_birth) < 1969:
	print "Lyndon B. Johnson was President when you were born"

if int(year_of_birth) >= 1969 and int(year_of_birth) < 1974:
	print "Richard Nixon was President when you were born"

if int(year_of_birth) >= 1974 and int(year_of_birth) < 1977:
	print "Gerald Ford was President when you were born"

if int(year_of_birth) >= 1977 and int(year_of_birth) < 1981:
	print "Jimmy Carter was President when you were born"

if int(year_of_birth) >= 1981 and int(year_of_birth) < 1989:
	print "Ronald Reagan was President when you were born"

if int(year_of_birth) >= 1989 and int(year_of_birth) < 1993:
	print "George H. W. Bush was President when you were born"


if int(year_of_birth) >= 1993 and int(year_of_birth) < 2001:
	print "Bill Clinton was President when you were born"

if int(year_of_birth) >= 2001 and int(year_of_birth) < 2009:
	print "Georg W. Bush was President when you were born"

if int(year_of_birth) >= 2009 and int(year_of_birth) < 2017:
	print "Barack Obama was President when you were born"


Obama = range(2009, 2017)
if int(year_of_birth) in Obama:
	print "hallo"

if int(year_of_birth) in range(2009, 2017):
	print "Barack Obama was President when you were born"






