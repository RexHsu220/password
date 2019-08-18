password = 'a123456'
i = 3 #Chances Left
while i > 0:
	i = i - 1
	pwd = input('Please enter your password: ')
	if pwd == password:
		print('Logged in Successfully')
		break
	else:
		print('Wrong Password !')
		if i > 0:
			print('You still have', i, 'chances')
		else: 
			print('No chances left !')
		 
