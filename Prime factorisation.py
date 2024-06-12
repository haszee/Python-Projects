'''
Prime Factorization - Have the user enter a number and find all Prime Factors (if there are any) and display them.
'''

while True:
	try:
		number = int(input('Enter a number: '))
		break
	except ValueError:
		print('Please enter an integer')

divlist = []

for x in range(2,int(number/2+1)): # up to half of number. No point in continuing further b/c any number greater than half (other than itself) will never be a factor
	if number%x == 0 and x not in divlist:
		divlist.append(x)
	for factor in divlist:
	 	if x in divlist and factor != x and x%factor == 0:
	 		divlist.remove(x)
		

print(f'All the Prime factors for {number} are: ', divlist)