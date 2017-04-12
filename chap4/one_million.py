# List of numbers from 1 to 1 million
numbers = list(range(1,1000001))
#print(numbers)
print(min(numbers))
print(max(numbers))
print(sum(numbers))
# Odd numbers from 1 to 20
numbers = list(range(1,20,2))
print(numbers)
# Multiple of 3 from 3 to 30
numbers = []
for number in range(3,31,3):
	numbers.append(number)
print(numbers)
# First 10 cubes
numbers = []
for number in range(1,11):
	numbers.append(number**3)
for number in numbers:
	print(number)
# List comprehension
numbers = [value**3 for value in range(1,11)]
print(numbers)