country = input('請問你的國家是？')
age = input('請問你的年齡是:')
age = int(age)
if country == '台灣':
	if age >= 18:
		print('你可以考駕照')
	else:
	 	print('你還不能考駕照')
elif country == '美國':
	if age >= 16:
		print('你可以考駕照')
	else:
		print('你還不能考駕照')
else:
	print('我不確定', country, '幾歲才能考駕照')