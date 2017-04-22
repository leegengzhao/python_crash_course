xiaotao = {
	'username':'xiaotaosun',
	'firstname':'xiaotao',
	'lastname':'sun',
	'age':'42',
	'city':'sammamish',
	}
for k, v in xiaotao.items():
	print("Key: " + k + ", " +
		"Value: " + v + 
		'.')
#for k in xiaotao.keys():
for k in sorted(xiaotao):	# default is to return keys
	print(k)
if 'sex' not in xiaotao.keys():
	print("Please specify sex")
	xiaotao['sex'] = 'female'
print(xiaotao)

favorite_languages_poll = {
	'jen':'python',
	'sarah':'c',
	'edward':'ruby',
	'phil':"python",
	'chad':"java",
	}
print("The following languages have been mentioned:")
for lan in set(favorite_languages_poll.values()):	# use set() to remove duplicates
	print(lan.title())
