# List of disctionaries
favorite_languages_poll = {
	'jen':['python', 'ruby'],
	'sarah':['c'],
	'edward':['ruby', 'perl'],
	'phil':["python", "java"],
	'chad':["c", 'c++', 'assembly'],
	}
for name, languages in favorite_languages_poll.items():
	if len(languages) > 1:
		print(name.title() + "'s favorite languages are:")
	else:
		print(name.title() + "'s favorite languages is:")
	for language in languages:
		print('\t' + language.title())

# A dictionary in a dictionary: username(email) as unique key, and
# poll info dictionary as the value
users_favorite_languages = {
	'jen@gmail.com': {
	'first_name': 'jen',
	'languages': ['python', 'ruby'],
	},
	'sarah@gmail.com': {
	'first_name': 'sarah',
	'languages': ['c'],
	},
	'edward@yahoo.com': {
	'first_name': 'edward',
	'languages': ['ruby', 'perl'],
	},
	'phil@yahoo.com': {
	'first_name': 'phil',
	'languages': ["python", "java"],
	},
	'chad@nokia.com': {
	'first_name': 'chad',
	'languages': ["c", 'c++', 'assembly'],
	},
	'sarah@yahoo.com': {
	'first_name': 'sarah',
	'languages': ['python', 'java'],
	},
}
for username, favorite_languages in users_favorite_languages.items():
	print("\nUsername: " + username)
	first_name = favorite_languages['first_name']
	languages = favorite_languages['languages']
	print('\tFirst name: ' + first_name)
	lan_display = ''
	for language in languages:
		if len(lan_display) > 0:
			lan_display += ', '
		lan_display += language.title()
	print('\tFavorite languages: ' + lan_display)
