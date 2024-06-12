'''
Fast Exponentiation - Ask the user to enter 2 integers a and b and output a^b (i.e. pow(a,b)) in O(lg n) time complexity
'''

x = int(input('Enter a number: '))
y = int(input('Enter another number: '))


def power(x,y):
	if y == 0:
		return 1
	else:
		n = power(x,y//2)
		if y%2 == 0:
			return  n**n
		else:
			x * n* n