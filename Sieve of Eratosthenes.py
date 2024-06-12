'''
Sieve of Eratosthenes - The sieve of Eratosthenes is one of the most efficient ways to find all of the smaller primes (below 10 million or so).
'''

n = int(input('Enter an integer: '))

def sieve(n):
	primelist = [True for i in range(n+1)]
	pos = 2 # both index position & corresponding number

	while pos*pos <= n:
		if primelist[pos] == True:
			for i in range(pos*pos,n+1,pos):
				primelist[i] = False
		pos += 1

	for i in range(2,n+1):
		if primelist[i]:
			print(i)

sieve(n)
