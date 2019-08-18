password = 'a123456'
i = 3 #Chances Left
while True:
	pwd = input('Please enter your password: ')
	if pwd == password:
		print('Logged in Successfully')
		break
	else:
		i = i - 1
		print('Wrong Password, you still have', i, 'chances')
		if i == 0:
			print('You have no chances left')
			break
