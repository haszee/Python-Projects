'''
Factorial Finder - The Factorial of a positive integer, n, is defined as the product of the sequence n, n-1, n-2, ...1 and the factorial of zero, 0, is defined as being 1. Solve this using both loops and recursion.
'''

number = int(input('Enter a number: '))

answer = 1

USING FOR LOOP
for factorial in range(number):
	answer *= (number)
	number -=1

USING RECURSION
def get_factorial(number,answer):
	if number > 0:
		answer = get_factorial(number-1,answer*number)
	return answer

print(get_factorial(number,answer))
