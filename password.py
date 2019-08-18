password = 'a123456'
i = 3 #Chances Left
while i > 0:
	pwd = input('Please enter your password: ')
	if pwd == password:
		print('Logged in Successfully')
		break
	else:
		i = i - 1
		print('Wrong Password, you still have', i, 'chances')
		 
