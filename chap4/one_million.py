# List of numbers from 1 to 1 million
million_numbers = list(range(1,1000001))
#print(million_numbers)
print(min(million_numbers))
print(max(million_numbers))
print(sum(million_numbers))
# Odd numbers from 1 to 20
odd_numbers = list(range(1,20,2))
print(odd_numbers)
# Multiple of 3 from 3 to 30
multi_3_numbers = []
for number in range(3,31,3):
    multi_3_numbers.append(number)
print(multi_3_numbers)
# First 10 cubes
cubes = []
for number in range(1,11):
    cubes.append(number**3)
for number in cubes:
    print(number)
# List comprehension
cubes = []
cubes = [value**3 for value in range(1,11)]
print(cubes)
# Copy list with slice
cubes_copy = cubes[:]
print(cubes_copy)
# First 3 and last 3
print(cubes_copy[0:3])
print(cubes[-3:])
# Make tuple from list
li=[1,2,'here is my name','lee zhao']
tup = tuple(li)
print(tup)    








