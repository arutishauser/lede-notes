numbers = [1, 2, 3, 4]

doubles = []
for number in numbers:
	doubles.append(number*2)
print doubles


results=[number*2 for number in numbers]
print results

doubless = []
for number in numbers:
	doubless.append(number*2)
print doubless


dogs = [
    { 'dog_name': 'Harry' },
    { 'dog_name': 'Trouble' },
    { 'dog_name': 'Toyota' },
    { 'dog_name': 'Brenda' }
]

results=[dog['dog_name'] for dog in dogs]
print results


names = []
for dog in dogs:
	doubless.append(dog['dog_name']*2)
print doubless