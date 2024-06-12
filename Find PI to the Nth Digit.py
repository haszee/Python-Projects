'''
Find PI to the Nth Digit - Enter a number and have the program generate pi up to that many decimal places. Keep a limit to how far the program will go.
'''

import math

while True:
	try:
		decimal = int(input('Enter the number of decimal places: '))
		break
	except ValueError:
		print('Please enter an integer')

print('The value of Pi is',round(math.pi, decimal),f'rounded to {decimal} decimal places')

