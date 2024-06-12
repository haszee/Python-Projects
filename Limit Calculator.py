'''
Limit Calculator - Ask the user to enter f(x) and the limit value, then return the value of the limit statement Optional: Make the calculator capable of supporting infinite limits.
'''

number = int(input('Enter a number f(x): '))

limit = int(input('Enter a number for limit: '))

def limit_calc(number):
	return (1+1/number)**number

for i in range(number,limit+1):
	print(limit_calc(i**2))
