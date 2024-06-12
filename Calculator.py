
'''
Calculator - A simple calculator to do basic operators. Make it a scientific calculator for added complexity.
'''

while True:
	try:
		decimal_1 = float(input('Enter a decimal number: '))
		break
	except ValueError:
		print('Please enter a number that has decimal places')

while True:
	try:
		operator = input('What calculation (+,-,x,/,^,!,log10,etc): ')
		break
	except ValueError:
		print('Please enter an operator')

while True:
	try:
		decimal_2 = float(input('Enter another decimal number: '))
		break
	except ValueError:
		print('Please enter a number that has decimal places')

if operator == '+':
	answer = decimal_1+decimal_2
elif operator == '-':
	answer = decimal_1-decimal_2
elif operator == 'x':
	answer = decimal_1*decimal_2
elif operator == '/':
	answer = decimal_1/decimal_2
elif operator == '^':
	answer = decimal_1**decimal_2
elif operator == '!':
	answer = 1
	for factorial in reversed(range(int(decimal_1))):
		answer = answer * (decimal_1)
		decimal_1 -=1
elif operator == 'log10':
	answer = 0
	while decimal_1 != 1:
		decimal_1 = decimal_1/10
		answer += 1		

print(f'The answer is {answer}')