'''
Binary to Decimal and Back Converter - Develop a converter to convert a decimal number to binary or a binary number to its decimal equivalent.
'''

while True:
	try:
		decimal = float(input('Enter a decimal number: '))
		break
	except ValueError:
		print('Please enter a number that has decimal places')

can also use bin() function to convert decimal to binary

def dectobin(number):
	reverse_binary = ''
	while number>=1:
		quotient = number//2
		remainder = str(int(number%2))
		number = quotient
		reverse_binary += remainder
	return reverse_binary[::-1]

binary = dectobin(decimal)
print(f'The binary value of {decimal} is {binary}')
		
while True:
	try:
		binary = input('Enter a binary number: ')
		break
	except ValueError:
		print('Please enter a binary number')

def bintodec(number):
	decimal = 0
	index = 0
	for power in reversed(range(len(number))):
		decimal = decimal + int(number[index]) * 2**power
		index += 1
	return decimal

decimal = bintodec(binary)
print(f'The decimal value of {binary} is {decimal}')