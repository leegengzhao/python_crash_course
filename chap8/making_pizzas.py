# import pizza
# from pizza import make_pizza
# from pizza import * # not recommended
import pizza as p

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushroom', 'green pepper', 'extra cheese')

# Function with arbitary number of keyword arguments
def build_profile(first_name, last_name, **user_info):
	"""Build and return a user profile dictionary"""
	profile = {}
	profile['first_name'] = first_name
	profile['last_name'] = last_name
	for key, value in user_info.items():
		profile[key] = value
	return profile

user_profile = build_profile('lee', 'zhao',
							location='sammamish',
							field='physics')
print("\n")
print(user_profile)
