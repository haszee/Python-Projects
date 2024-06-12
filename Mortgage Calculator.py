'''
Mortgage Calculator - Calculate the monthly payments of a fixed term mortgage over given Nth terms at a given interest rate. Also figure out how long it will take the user to pay back the loan. For added complexity, add an option for users to select the compounding interval (Monthly, Weekly, Daily, Continually).
'''

while True:
	try:
		mortgage = float(input('Enter the mortgage: '))
		break
	except ValueError:
		print('Please enter a number that has decimal places')


while True:
	try:
		interest = float(input('Enter the interest rate: '))/100
		break
	except ValueError:
		print('Please enter a number that has decimal places')


while True:
	try:
		term = int(input('Enter the length of the mortgage: '))
		break
	except ValueError:
		print('Please enter a number that has decimal places')

while True:
	try:
		interval = input('Enter the compounding interval (monthly, weekly or daily): ')
		break
	except ValueError:
		print('Please enter an integer')

if interval == 'monthly':
	interval = 12
elif interval == 'weekly':
	interval = 52
elif interval == 'daily':
	interval = 365

#payment is (principle * (interest/interval))/(1-(1+interest/interval)^(-interval*term))

payment = round((mortgage*interest/interval)/(1-(1+interest/interval)**(-interval*term)),2)

print(f'Monthly payment is ${payment}.')