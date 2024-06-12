'''
Unit Converter (temp, currency, volume, mass and more) - Converts various units between one another. The user enters the type of unit being entered, the type of unit they want to convert to and then the value. The program will then make the conversion.
'''

while True:
	try:
		number = float(input('Enter a decimal number: '))
		break
	except ValueError:
		print('Please enter a number that has decimal places')

while True:
	try:
		unit_1 = input('What unit is the number (C,F,radius,inch,feet,cm, m): ')
		break
	except ValueError:
		print('Please enter a unit')

while True:
	try:
		unit_2 = input('What unit would you like to convert it into (C,F,volume,circumference, inch, feet, cm, m): ')
		break
	except ValueError:
		print('Please enter a unit')

if unit_2 == 'C' or 'c':
	celsius = (number-32) * 5/9
elif unit_2 == 'F' or 'f':
	farenheit = number*9/5 + 32
elif unit_1 == 'radius' or 'r':
	if unit_2 == 'volume' or 'v':
		volume = 4/3*3.14*number**3
	elif unit_2 == 'circumference':
		volume = 3.14*number**2