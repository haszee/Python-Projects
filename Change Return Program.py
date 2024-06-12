'''
Change Return Program - The user enters a cost and then the amount of money given. The program will figure out the change and the number of quarters, dimes, nickels, pennies needed for the change.
'''

while True:
	try:
		cost = float(input('Enter the cost of the good: '))
		break
	except ValueError:
		print('Please enter a number that has decimal places')

while True:
	try:
		payment = float(input('Enter the amount of money given: '))
		break
	except ValueError:
		print('Please enter a number that has decimal places')

change_val = round(payment-cost,2)

quarters_val = 0.25
dimes_val = 0.1
nickels_val = 0.05
pennies_val = 0.01

def check_change(change):
	if change != 0:
		return True
	else:
		return False

def calc_change(change,coinvalue):
	if check_change(change):
		coin_num = change//coinvalue
		new_change = update_change(change,coin_num,coinvalue)
		return coin_num,new_change
	else: 
		return 0,0

def update_change(change,coin_num,coinvalue):
	new_change = change - coin_num*coinvalue
	return new_change

quarters,new_change = calc_change(change_val,quarters_val)
dimes,new_change = calc_change(new_change,dimes_val)
nickels,new_change = calc_change(new_change,nickels_val)
pennies,new_change = calc_change(new_change,pennies_val)

print(f'The total change is {change_val}. This is divided into:\n{quarters} quarters\n{dimes} dimes\n{nickels} nickels\n{pennies} pennies')