'''
Find e to the Nth Digit - Just like the previous problem, but with e instead of π (pi). Enter a number and have the program generate e up to that many decimal places. Keep a limit to how far the program will go
'''

while True:
	try:
		number = float(input('Enter a decimal number: '))
		break
	except ValueError:
		print('Please enter a number that has decimal places')


while True:
	try:
		decimal = int(input('Enter the number of decimal places: '))
		break
	except ValueError:
		print('Please enter an integer')

print(f'The value of {number} to {decimal} decimal places is',round(number, decimal))