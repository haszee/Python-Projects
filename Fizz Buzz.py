'''
Fizz Buzz - Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”.
'''

def fizzbuzz(num):
if num%3 == 0 and num%5 == 0:
	return 'FizzBuzz'
elif num%3 == 0 and not num%5== 0:
	return 'Fizz'
elif num%5 == 0 and not num%3 == 0:
	return 'Buzz'
else:
	return num

for num in range(1,101):
checknum = fizzbuzz(num)
print(checknum)