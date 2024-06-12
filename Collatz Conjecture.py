'''
Collatz Conjecture - Start with a number n > 1. Find the number of steps it takes to reach one using the following process: If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1.
'''

while True:
	try:
		number = int(input('Enter a number greater than 1: '))
		assert number > 1
		break
	except:
		print('Wrong number')

# USING RECURSION
def collatz(number,count = 0):
    if number == 1:
        return count
    if number%2 == 0:
        return collatz(number/2,count+1)   
    else:
        return collatz(number*3+1,count+1)

count = collatz(number)

USING WHILE LOOP
count = 0

while number != 1:
	if number%2 == 0:
		number /= 2
	else:
		number = 3*number + 1
	print(number)
	count += 1

print(count)


