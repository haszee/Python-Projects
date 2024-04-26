'''
Find PI to the Nth Digit - Enter a number and have the program generate pi up to that many decimal places. Keep a limit to how far the program will go.
'''

# import math

# while True:
# 	try:
# 		decimal = int(input('Enter the number of decimal places: '))
# 		break
# 	except ValueError:
# 		print('Please enter an integer')

# print('The value of Pi is',round(math.pi, decimal),f'rounded to {decimal} decimal places')

#-------------------------------------------------------------------------

'''
Find e to the Nth Digit - Just like the previous problem, but with e instead of π (pi). Enter a number and have the program generate e up to that many decimal places. Keep a limit to how far the program will go
'''

# while True:
# 	try:
# 		number = float(input('Enter a decimal number: '))
# 		break
# 	except ValueError:
# 		print('Please enter a number that has decimal places')


# while True:
# 	try:
# 		decimal = int(input('Enter the number of decimal places: '))
# 		break
# 	except ValueError:
# 		print('Please enter an integer')

# print(f'The value of {number} to {decimal} decimal places is',round(number, decimal))

#-------------------------------------------------------------------------

'''
Fibonacci Sequence - Enter a number and have the program generate the Fibonacci sequence to that number or to the Nth number.
'''

# while True:
# 	try:
# 		number = int(input('Enter a number: '))
# 		break
# 	except ValueError:
# 		print('Please enter an integer')

# fib = 1 # fibonnaci number
# n = 1 # nth term

# for num in range(0,number):
# 	print(fib)
# 	current_fib = fib # saves the current fib so we can add it to n
# 	fib = n # updates the future fib to n
# 	n += current_fib # updates n

#-------------------------------------------------------------------------

'''
Prime Factorization - Have the user enter a number and find all Prime Factors (if there are any) and display them.
'''

# while True:
# 	try:
# 		number = int(input('Enter a number: '))
# 		break
# 	except ValueError:
# 		print('Please enter an integer')

# divlist = []

# for x in range(2,int(number/2+1)): # up to half of number. No point in continuing further b/c any number greater than half (other than itself) will never be a factor
# 	if number%x == 0 and x not in divlist:
# 		divlist.append(x)
# 	for factor in divlist:
# 	 	if x in divlist and factor != x and x%factor == 0:
# 	 		divlist.remove(x)
		

# print(f'All the Prime factors for {number} are: ', divlist)

#-------------------------------------------------------------------------

'''
Next Prime Number - Have the program find prime numbers until the user chooses to stop asking for the next one.
'''

# def check_prime(num, primes):
# 	for factor in range(2,num+1):
# 		if num%factor == 0 and factor not in primes:
# 			primes.append(factor)
# 		for p_num in primes:
# 			if factor in primes and p_num != factor and factor%p_num == 0:
# 				primes.remove(factor)
# 	return primes

# def ask_continue():
# 	while True:
# 		try:
# 			next_num = input('Do you wish get the next prime number (y or n): ')
# 			break
# 		except ValueError:
# 			print('Please enter either y or n')
# 	return next_num

# def get_prime(num, primes):
# 	print(num)
# 	if num not in primes:
# 		primes = check_prime(num, primes)
# 	num += 1
# 	return num, primes

# primes = []
# num = 2	

# while True:
# 	next_num = ask_continue()
# 	if next_num == 'y':
# 		print(next_num)
# 		num, primes = get_prime(num, primes)
# 	else:
# 		break
# print(primes)

#-------------------------------------------------------------------------

'''
Find Cost of Tile to Cover W x H Floor - Calculate the total cost of tile it would take to cover a floor plan of width and height, using a cost entered by the user.
'''

# while True:
# 	try:
# 		price = float(input('Enter the cost of 1 tile: '))
# 		break
# 	except ValueError:
# 		print('Please enter a number that has decimal places')

# while True:
# 	try:
# 		width = float(input('Enter the width of the floor: '))
# 		break
# 	except ValueError:
# 		print('Please enter a number that has decimal places')

# while True:
# 	try:
# 		length = float(input('Enter the length of the floor: '))
# 		break
# 	except ValueError:
# 		print('Please enter a number that has decimal places')

# # assume each tile is 1x1
# area_tile = 1
# area_floor = width * length

# tile_cost = price/area_tile

# floor_cost = tile_cost * area_floor

# print(f'The total cost of tiles to cover an area (WxH) {width}x{length} is ${floor_cost}.')

#-------------------------------------------------------------------------

'''
Mortgage Calculator - Calculate the monthly payments of a fixed term mortgage over given Nth terms at a given interest rate. Also figure out how long it will take the user to pay back the loan. For added complexity, add an option for users to select the compounding interval (Monthly, Weekly, Daily, Continually).
'''

# while True:
# 	try:
# 		mortgage = float(input('Enter the mortgage: '))
# 		break
# 	except ValueError:
# 		print('Please enter a number that has decimal places')


# while True:
# 	try:
# 		interest = float(input('Enter the interest rate: '))/100
# 		break
# 	except ValueError:
# 		print('Please enter a number that has decimal places')


# while True:
# 	try:
# 		term = int(input('Enter the length of the mortgage: '))
# 		break
# 	except ValueError:
# 		print('Please enter a number that has decimal places')

# while True:
# 	try:
# 		interval = input('Enter the compounding interval (monthly, weekly or daily): ')
# 		break
# 	except ValueError:
# 		print('Please enter an integer')

# if interval == 'monthly':
# 	interval = 12
# elif interval == 'weekly':
# 	interval = 52
# elif interval == 'daily':
# 	interval = 365

# #payment is (principle * (interest/interval))/(1-(1+interest/interval)^(-interval*term))

# payment = round((mortgage*interest/interval)/(1-(1+interest/interval)**(-interval*term)),2)

# print(f'Monthly payment is ${payment}.')

#-------------------------------------------------------------------------

'''
Change Return Program - The user enters a cost and then the amount of money given. The program will figure out the change and the number of quarters, dimes, nickels, pennies needed for the change.
'''

# while True:
# 	try:
# 		cost = float(input('Enter the cost of the good: '))
# 		break
# 	except ValueError:
# 		print('Please enter a number that has decimal places')

# while True:
# 	try:
# 		payment = float(input('Enter the amount of money given: '))
# 		break
# 	except ValueError:
# 		print('Please enter a number that has decimal places')

# change_val = round(payment-cost,2)

# quarters_val = 0.25
# dimes_val = 0.1
# nickels_val = 0.05
# pennies_val = 0.01

# def check_change(change):
# 	if change != 0:
# 		return True
# 	else:
# 		return False

# def calc_change(change,coinvalue):
# 	if check_change(change):
# 		coin_num = change//coinvalue
# 		new_change = update_change(change,coin_num,coinvalue)
# 		return coin_num,new_change
# 	else: 
# 		return 0,0

# def update_change(change,coin_num,coinvalue):
# 	new_change = change - coin_num*coinvalue
# 	return new_change

# quarters,new_change = calc_change(change_val,quarters_val)
# dimes,new_change = calc_change(new_change,dimes_val)
# nickels,new_change = calc_change(new_change,nickels_val)
# pennies,new_change = calc_change(new_change,pennies_val)

# print(f'The total change is {change_val}. This is divided into:\n{quarters} quarters\n{dimes} dimes\n{nickels} nickels\n{pennies} pennies')

#-------------------------------------------------------------------------

'''
Binary to Decimal and Back Converter - Develop a converter to convert a decimal number to binary or a binary number to its decimal equivalent.
'''

# while True:
# 	try:
# 		decimal = float(input('Enter a decimal number: '))
# 		break
# 	except ValueError:
# 		print('Please enter a number that has decimal places')

#can also use bin() function to convert decimal to binary

# def dectobin(number):
# 	reverse_binary = ''
# 	while number>=1:
# 		quotient = number//2
# 		remainder = str(int(number%2))
# 		number = quotient
# 		reverse_binary += remainder
# 	return reverse_binary[::-1]

# binary = dectobin(decimal)
# print(f'The binary value of {decimal} is {binary}')
		
# while True:
# 	try:
# 		binary = input('Enter a binary number: ')
# 		break
# 	except ValueError:
# 		print('Please enter a binary number')

# def bintodec(number):
# 	decimal = 0
# 	index = 0
# 	for power in reversed(range(len(number))):
# 		decimal = decimal + int(number[index]) * 2**power
# 		index += 1
# 	return decimal

# decimal = bintodec(binary)
# print(f'The decimal value of {binary} is {decimal}')

#-------------------------------------------------------------------------

'''
Calculator - A simple calculator to do basic operators. Make it a scientific calculator for added complexity.'''

# while True:
# 	try:
# 		decimal_1 = float(input('Enter a decimal number: '))
# 		break
# 	except ValueError:
# 		print('Please enter a number that has decimal places')

# while True:
# 	try:
# 		operator = input('What calculation (+,-,x,/,^,!,log10,etc): ')
# 		break
# 	except ValueError:
# 		print('Please enter an operator')

# while True:
# 	try:
# 		decimal_2 = float(input('Enter another decimal number: '))
# 		break
# 	except ValueError:
# 		print('Please enter a number that has decimal places')

# if operator == '+':
# 	answer = decimal_1+decimal_2
# elif operator == '-':
# 	answer = decimal_1-decimal_2
# elif operator == 'x':
# 	answer = decimal_1*decimal_2
# elif operator == '/':
# 	answer = decimal_1/decimal_2
# elif operator == '^':
# 	answer = decimal_1**decimal_2
# elif operator == '!':
# 	answer = 1
# 	for factorial in reversed(range(int(decimal_1))):
# 		answer = answer * (decimal_1)
# 		decimal_1 -=1
# elif operator == 'log10':
# 	answer = 0
# 	while decimal_1 != 1:
# 		decimal_1 = decimal_1/10
# 		answer += 1		

# print(f'The answer is {answer}')

#-------------------------------------------------------------------------

'''
Unit Converter (temp, currency, volume, mass and more) - Converts various units between one another. The user enters the type of unit being entered, the type of unit they want to convert to and then the value. The program will then make the conversion.
'''

# while True:
# 	try:
# 		number = float(input('Enter a decimal number: '))
# 		break
# 	except ValueError:
# 		print('Please enter a number that has decimal places')

# while True:
# 	try:
# 		unit_1 = input('What unit is the number (C,F,radius,inch,feet,cm, m): ')
# 		break
# 	except ValueError:
# 		print('Please enter a unit')

# while True:
# 	try:
# 		unit_2 = input('What unit would you like to convert it into (C,F,volume,circumference, inch, feet, cm, m): ')
# 		break
# 	except ValueError:
# 		print('Please enter a unit')

# if unit_2 == 'C' or 'c':
# 	celsius = (number-32) * 5/9
# elif unit_2 == 'F' or 'f':
# 	farenheit = number*9/5 + 32
# elif unit_1 == 'radius' or 'r':
# 	if unit_2 == 'volume' or 'v':
# 		volume = 4/3*3.14*number**3
# 	elif unit_2 == 'circumference':
# 		volume = 3.14*number**2

#-------------------------------------------------------------------------

'''
Alarm Clock - A simple clock where it plays a sound after X number of minutes/seconds or at a particular time.
'''

# import time, datetime, winsound, os, platform

# def main():

# 	while True:
# 		try:
# 			set_alarm = input('Enter what time to wake up in 24 hr format (hr:min:sec): ').split(':')
# 			break
# 		except ValueError:
# 			print('Please enter the time')

# 	alarm_time = datetime.time(int(set_alarm[0]),int(set_alarm[1]),int(set_alarm[2]))

	
# 	alarm(alarm_time)

# def alarm(alarm_time):
# 	current_time = datetime.datetime.now().time()
# 	current_hour = current_time.hour
# 	current_min = current_time.minute
# 	current_sec = current_time.second

# 	start_time = current_hour*3600 + current_min * 60 + current_sec
# 	end_time = alarm_time.hour*3600 + alarm_time.minute*60 + alarm_time.second
# 	elapsed_time = end_time - start_time

# 	print(f'The current time is {current_time}')
# 	print(f'Alarm is set for {alarm_time}')
# 	time.sleep(elapsed_time)
# 	sound()

# def sound():
# 	for repeats in range(3):
# 		for beeps in range(10):
# 			winsound.MessageBeep(1)
# 			time.sleep(2)
# 		time.sleep(60)

# main()

#-------------------------------------------------------------------------

'''
Distance Between Two Cities - Calculates the distance between two cities and allows the user to specify a unit of distance. This program may require finding coordinates for the cities like latitude and longitude.
'''

# from pygeocoder import Geocoder
# import sys
# from math import radians, sin, cos, sqrt, atan2


# def get_distance(lat1, lon1, lat2, lon2):
# 	R = 6371  # Earth radius in kilometers
# 	dlat = radians(lat2 - lat1)
# 	dlon = radians(lon2 - lon1)
# 	a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
# 	c = 2 * atan2(sqrt(a), sqrt(1 - a))
# 	distance = R * c
# 	return distance

# def main():
# 	city1 = input('Enter a city: ')
# 	city2 = input('Enter another city: ')
# 	units = input('Enter the units (kilometers(km) or miles(m)): ')

# 	city1_loc = Geocoder.geocode(city1)[0].coordinates
# 	city2_loc = Geocoder.geocode(city2)[0].coordinates

# 	print(city1_loc)
# 	print(city2_loc)


# 	print('The latitude of Edmonton is: ', location1.latitude)
# 	print('The longitude of Edmonton is: ', location1.longitude,'\n')

# 	print('The latitude of Calgary is: ', location2.latitude)
# 	print('The longitude of Calgary is: ', location2.longitude)

# 	distance = get_distance(location1.latitude,location1.longitude,location2.latitude,location2.longitude)

# if __name__ == '__main__':
# 	sys.exit(main())


#-------------------------------------------------------------------------

'''
Credit Card Validator - Takes in a credit card number from a common credit card vendor (Visa, MasterCard, American Express, Discoverer) and validates it to make sure that it is a valid number (look into how credit cards use a checksum)
'''

# card_num = input('Enter your credit card number: ')

# total = 0
# for num in card_num[-2::-2]: #iterates backwards starting from second last number
# 	double = int(num)*2
# 	if double > 9:
# 		dig1 = double//10
# 		dig2 = double%10
# 		total = total + dig1 + dig2
# 	else:
# 		total += double

# for num in card_num[::-2]:
# 	total += int(num)

# # print(total)
# if total%10 == 0:
# 	print('This is a valid credit card.')
# else:
# 	print('Warning! This is not a valid credit card number!')

#-------------------------------------------------------------------------

'''
Tax Calculator - Asks the user to enter a cost and either a country or state tax. It then returns the tax plus the total cost with tax.
'''

# cost = float(input('Enter the cost of the product: '))
# tax =  float(input('Enter the tax rate: '))/100

# final_cost = cost + cost*tax
# print(final_cost)

#-------------------------------------------------------------------------

'''
Factorial Finder - The Factorial of a positive integer, n, is defined as the product of the sequence n, n-1, n-2, ...1 and the factorial of zero, 0, is defined as being 1. Solve this using both loops and recursion.
'''

# number = int(input('Enter a number: '))

# answer = 1

# USING FOR LOOP
# for factorial in range(number):
# 	answer *= (number)
# 	number -=1

# USING RECURSION
# def get_factorial(number,answer):
# 	if number > 0:
# 		answer = get_factorial(number-1,answer*number)
# 	return answer

# print(get_factorial(number,answer))

#-------------------------------------------------------------------------

'''
Happy Numbers - A happy number is defined by the following process. Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers, while those that do not end in 1 are unhappy numbers. Display an example of your output here. Find first 8 happy numbers.
'''

# while True:
# 	try:
# 		number = int(input('Enter a number: '))
# 		break
# 	except ValueError:
# 		print('Please enter an integer')

# while True:
#     dig_sum = 0
#     for digit in str(number):
#         dig_sum += int(digit)**2
#     if dig_sum == 1:
#     	print('Happy number:')
#     	break
#     elif dig_sum != 1 and len(str(dig_sum)) < 2:
#     	print('Unhappy number')
#     	break
#     else:
#         number = dig_sum

# print(dig_sum)

#-------------------------------------------------------------------------

'''
Number Names - Show how to spell out a number in English. You can use a preexisting implementation or roll your own, but you should support inputs up to at least one million (or the maximum value of your language's default bounded integer type, if that's less). Optional: Support for inputs other than positive integers (like zero, negative integers, and floating-point numbers).
'''

# while True:
# 	try:
# 		number = input('Enter a number: ')
# 		break
# 	except ValueError:
# 		print('Please enter a positive or negative number less than or equal to 1,000,000')

# if '-' in number:
# 	words = '-'
# 	number = str(abs(int(number)))
# else:
# 	words = ''

# onesPlaces = ['','one','two','three','four','five','six','seven','eight','nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen','sixteen', 'seventeen', 'eighteen', 'nineteen']
# tensPlaces = ['and', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

# def one_Places(number):
# 	places = onesPlaces[int(number)]
# 	return places

# def ten_Places(number):
# 	if int(number)%10 == 0:
# 		dig = int(number)/10
# 		places = tensPlaces[int(dig)]
# 	elif int(number) <= 19 and int(number) >= 11:
# 		places = onesPlaces[int(number)]
# 	else:
# 		dig_tens = int(number)//10
# 		dig_ones = int(number)%10
# 		places = tensPlaces[dig_tens] + ' ' + onesPlaces[dig_ones]
# 	return places

# def hun_Places(number):
# 	if number != 0:
# 		if number%100 == 0:
# 			dig_hun = int(number)//100
# 			places = f'{onesPlaces[dig_hun]} hundred'
# 		else:
# 			dig_hun = int(number)//100
# 			places_huns = f'{onesPlaces[dig_hun]} hundred'
# 			tempnum = int(number)%100
# 			places_tens = ten_Places(tempnum)
# 			places = places_huns + ' ' + places_tens
# 	else:
# 		places = ''
# 	return places

# def thous_Places(number):
# 	if len(number) == 5:
# 		places_thous = f'{ten_Places(int(number)//1000)} thousand'
# 	elif len(number) == 4:
# 		if int(number)%10 == 0:
# 			dig = int(number)//1000
# 			places_thous = f'{onesPlaces[dig]} thousand'
# 		else:
# 			dig = int(number)//1000
# 			places_thous = f'{onesPlaces[dig]} thousand'
# 	tempnum = str(int(number)%1000)
# 	if len(tempnum) == 1:
# 		places2 = 'and ' + one_Places(int(tempnum))
# 	elif len(tempnum) == 2:
# 		places2 = 'and ' + ten_Places(int(tempnum))
# 	elif len(tempnum) == 3:
# 		places2 = hun_Places(int(tempnum))
# 	places = places_thous + ' ' + places2
# 	return places

# def hunthous_Places(number):
# 	if int(number)%100000 == 0:
# 		dig = int(number)//100000
# 		places = f'{onesPlaces[dig]}-hundred thousand'
# 	else:
# 		dig1 = int(number)//1000
# 		places1 = f'{hun_Places(dig1)} thousand'
		
# 		tempnum = int(number)%1000
# 		if len(str(tempnum)) == 1 and tempnum != 0:
# 			places2 = 'and ' + one_Places(tempnum)
# 		elif len(str(tempnum)) == 1 and tempnum == 0:
# 			places2 = one_Places(tempnum)
# 		elif len(str(tempnum)) == 2:
# 			places2 = ten_Places(tempnum)
# 		elif len(str(tempnum)) == 3:
# 			places2 = hun_Places(tempnum)
# 		places = places1 + ' ' + places2
# 	return places

# def mil_Places(number):
# 	dig = int(number)//1000000
# 	places1 = f'{onesPlaces[dig]} million'
	
# 	tempnum = int(number)%1000000

# 	if len(str(tempnum)) == 1 and tempnum != 0:
# 		places2 = 'and ' + one_Places(tempnum)
# 	elif len(str(tempnum)) == 1 and tempnum == 0:
# 		places2 = one_Places(tempnum)
# 	elif len(str(tempnum)) == 2:
# 		places2 = ten_Places(tempnum)
# 	elif len(str(tempnum)) == 3:
# 		places2 = hun_Places(tempnum)
# 	elif len(str(tempnum)) == 4 or len(str(tempnum)) == 5:
# 		places2 = thous_Places(tempnum)
# 	elif len(str(tempnum)) == 6:
# 		places2 = hunthous_Places(tempnum)
# 	places = places1 + ' ' + places2
# 	return places

# if len(number) == 1:
# 	places = one_Places(number)
# elif len(number) == 2:
# 	places = ten_Places(number)
# elif len(number) == 3:
# 	places = hun_Places(number)
# elif len(number) == 4:
# 	places = thous_Places(number)
# elif len(number) == 5:
# 	places = thous_Places(number)
# elif len(number) == 6:
# 	places = hunthous_Places(number)
# elif len(number) == 7:
# 	places = mil_Places(number)

# words += places

# print(words)

#-------------------------------------------------------------------------

'''
Coin Flip Simulation - Write some code that simulates flipping a single coin however many times the user decides. The code should record the outcomes and count the number of tails and heads.
'''

# import random

# count_heads = 0
# count_tails = 0

# heads = 1
# tails = 0

# while True:
# 	flip = random.randint(0,1)
# 	if flip == 1:
# 		count_heads += 1
# 		print(f'heads: {count_heads}')
# 	else:
# 		count_tails += 1
# 		print(f'tails: {count_tails}')
# 	ask_flip = input('Do you wish to flip again? (y or no?) ').lower()
# 	if ask_flip == 'y':
# 		continue
# 	else:
# 		break

#-------------------------------------------------------------------------

'''
Limit Calculator - Ask the user to enter f(x) and the limit value, then return the value of the limit statement Optional: Make the calculator capable of supporting infinite limits.
'''

# number = int(input('Enter a number f(x): '))

# limit = int(input('Enter a number for limit: '))

# def limit_calc(number):
# 	return (1+1/number)**number

# for i in range(number,limit+1):
# 	print(limit_calc(i**2))

#-------------------------------------------------------------------------

'''
Fast Exponentiation - Ask the user to enter 2 integers a and b and output a^b (i.e. pow(a,b)) in O(lg n) time complexity
'''

# x = int(input('Enter a number: '))
# y = int(input('Enter another number: '))


# def power(x,y):
# 	if y == 0:
# 		return 1
# 	else:
# 		n = power(x,y//2)
# 		if y%2 == 0:
# 			return  n**n
# 		else:
# 			x * n* n


