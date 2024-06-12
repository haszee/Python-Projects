'''
Next Prime Number - Have the program find prime numbers until the user chooses to stop asking for the next one.
'''

def check_prime(num, primes):
	for factor in range(2,num+1):
		if num%factor == 0 and factor not in primes:
			primes.append(factor)
		for p_num in primes:
			if factor in primes and p_num != factor and factor%p_num == 0:
				primes.remove(factor)
	return primes

def ask_continue():
	while True:
		try:
			next_num = input('Do you wish get the next prime number (y or n): ')
			break
		except ValueError:
			print('Please enter either y or n')
	return next_num

def get_prime(num, primes):
	if num not in primes:
		primes = check_prime(num, primes)
	num += 1
	return num, primes

primes = []
num = 2	

while True:
	next_num = ask_continue()
	if next_num == 'y':
		num, primes = get_prime(next_num, primes)
	else:
		break
print(primes)