'''
Happy Numbers - A happy number is defined by the following process. Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers, while those that do not end in 1 are unhappy numbers. Display an example of your output here. Find first 8 happy numbers.
'''

while True:
	try:
		number = int(input('Enter a number: '))
		break
	except ValueError:
		print('Please enter an integer')

while True:
    dig_sum = 0
    for digit in str(number):
        dig_sum += int(digit)**2
    if dig_sum == 1:
    	print('Happy number:')
    	break
    elif dig_sum != 1 and len(str(dig_sum)) < 2:
    	print('Unhappy number')
    	break
    else:
        number = dig_sum

print(dig_sum)