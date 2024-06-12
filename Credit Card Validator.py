'''
Credit Card Validator - Takes in a credit card number from a common credit card vendor (Visa, MasterCard, American Express, Discoverer) and validates it to make sure that it is a valid number (look into how credit cards use a checksum)
'''

card_num = input('Enter your credit card number: ')

total = 0
for num in card_num[-2::-2]: #iterates backwards starting from second last number
	double = int(num)*2
	if double > 9:
		dig1 = double//10
		dig2 = double%10
		total = total + dig1 + dig2
	else:
		total += double

for num in card_num[::-2]:
	total += int(num)

# print(total)
if total%10 == 0:
	print('This is a valid credit card.')
else:
	print('Warning! This is not a valid credit card number!')