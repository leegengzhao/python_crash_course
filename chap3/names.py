dinner_invites = ['you jin','deng xueping','lin xiaoning']
# reply_no_name='deng xueping'
# dinner_invites.remove(reply_no_name)
# print(reply_no_name.title()+" can't make it")
# dinner_invites.append('todd smith')

# for name in dinner_invites:
# 	print("Dear "+name.title()+", I'd like to invite you to come to our house for dinner.")

# while len(dinner_invites) > 2:
# 	name=dinner_invites.pop()
# 	print("Dear "+name.title()+", I am sorry but I can't invite you to dinner.")

print(dinner_invites)
# Temporary sort
print(sorted(dinner_invites))
print(sorted(dinner_invites,reverse=True))
print(dinner_invites)

# Permanent sort
# the two lines below don't work as intended and prinnts out None!
# print(dinner_invites.sort())
# print(dinner_invites.sort(reverse=True))
dinner_invites.sort()
print(dinner_invites)
dinner_invites.sort(reverse=True)
print(dinner_invites)
dinner_invites.reverse()
print(dinner_invites)
print(dinner_invites)

	
