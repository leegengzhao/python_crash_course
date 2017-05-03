# The asterick in the parameter name tells Python to make an empty tuple
# called toppings and pack wahtever values it receives into this tuple.
def make_pizza(size, *toppings):
	"""Pizza items"""
	print("\nmaking a " + str(size) +
		"-inch pizza with the following toppings:")
	for topping in toppings:
		print("- " + topping)
