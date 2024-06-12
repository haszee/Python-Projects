'''
Number Names - Show how to spell out a number in English. You can use a preexisting implementation or roll your own, but you should support inputs up to at least one million (or the maximum value of your language's default bounded integer type, if that's less). Optional: Support for inputs other than positive integers (like zero, negative integers, and floating-point numbers).
'''

while True:
	try:
		number = input('Enter a number: ')
		break
	except ValueError:
		print('Please enter a positive or negative number less than or equal to 1,000,000')

if '-' in number:
	words = '-'
	number = str(abs(int(number)))
else:
	words = ''

onesPlaces = ['','one','two','three','four','five','six','seven','eight','nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen','sixteen', 'seventeen', 'eighteen', 'nineteen']
tensPlaces = ['and', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

def one_Places(number):
	places = onesPlaces[int(number)]
	return places

def ten_Places(number):
	if int(number)%10 == 0:
		dig = int(number)/10
		places = tensPlaces[int(dig)]
	elif int(number) <= 19 and int(number) >= 11:
		places = onesPlaces[int(number)]
	else:
		dig_tens = int(number)//10
		dig_ones = int(number)%10
		places = tensPlaces[dig_tens] + ' ' + onesPlaces[dig_ones]
	return places

def hun_Places(number):
	if number != 0:
		if number%100 == 0:
			dig_hun = int(number)//100
			places = f'{onesPlaces[dig_hun]} hundred'
		else:
			dig_hun = int(number)//100
			places_huns = f'{onesPlaces[dig_hun]} hundred'
			tempnum = int(number)%100
			places_tens = ten_Places(tempnum)
			places = places_huns + ' ' + places_tens
	else:
		places = ''
	return places

def thous_Places(number):
	if len(number) == 5:
		places_thous = f'{ten_Places(int(number)//1000)} thousand'
	elif len(number) == 4:
		if int(number)%10 == 0:
			dig = int(number)//1000
			places_thous = f'{onesPlaces[dig]} thousand'
		else:
			dig = int(number)//1000
			places_thous = f'{onesPlaces[dig]} thousand'
	tempnum = str(int(number)%1000)
	if len(tempnum) == 1:
		places2 = 'and ' + one_Places(int(tempnum))
	elif len(tempnum) == 2:
		places2 = 'and ' + ten_Places(int(tempnum))
	elif len(tempnum) == 3:
		places2 = hun_Places(int(tempnum))
	places = places_thous + ' ' + places2
	return places

def hunthous_Places(number):
	if int(number)%100000 == 0:
		dig = int(number)//100000
		places = f'{onesPlaces[dig]}-hundred thousand'
	else:
		dig1 = int(number)//1000
		places1 = f'{hun_Places(dig1)} thousand'
		
		tempnum = int(number)%1000
		if len(str(tempnum)) == 1 and tempnum != 0:
			places2 = 'and ' + one_Places(tempnum)
		elif len(str(tempnum)) == 1 and tempnum == 0:
			places2 = one_Places(tempnum)
		elif len(str(tempnum)) == 2:
			places2 = ten_Places(tempnum)
		elif len(str(tempnum)) == 3:
			places2 = hun_Places(tempnum)
		places = places1 + ' ' + places2
	return places

def mil_Places(number):
	dig = int(number)//1000000
	places1 = f'{onesPlaces[dig]} million'
	
	tempnum = int(number)%1000000

	if len(str(tempnum)) == 1 and tempnum != 0:
		places2 = 'and ' + one_Places(tempnum)
	elif len(str(tempnum)) == 1 and tempnum == 0:
		places2 = one_Places(tempnum)
	elif len(str(tempnum)) == 2:
		places2 = ten_Places(tempnum)
	elif len(str(tempnum)) == 3:
		places2 = hun_Places(tempnum)
	elif len(str(tempnum)) == 4 or len(str(tempnum)) == 5:
		places2 = thous_Places(tempnum)
	elif len(str(tempnum)) == 6:
		places2 = hunthous_Places(tempnum)
	places = places1 + ' ' + places2
	return places

if len(number) == 1:
	places = one_Places(number)
elif len(number) == 2:
	places = ten_Places(number)
elif len(number) == 3:
	places = hun_Places(number)
elif len(number) == 4:
	places = thous_Places(number)
elif len(number) == 5:
	places = thous_Places(number)
elif len(number) == 6:
	places = hunthous_Places(number)
elif len(number) == 7:
	places = mil_Places(number)

words += places

print(words)