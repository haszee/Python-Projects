'''
Fibonacci Sequence - Enter a number and have the program generate the Fibonacci sequence to that number or to the Nth number.
'''

while True:
	try:
		number = int(input('Enter a number: '))
		break
	except ValueError:
		print('Please enter an integer')

fib = 1 # fibonnaci number
n = 1 # nth term

for num in range(0,number):
	print(fib)
	current_fib = fib # saves the current fib so we can add it to n
	fib = n # updates the future fib to n
	n += current_fib # updates n