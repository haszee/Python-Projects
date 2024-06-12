'''
Coin Flip Simulation - Write some code that simulates flipping a single coin however many times the user decides. The code should record the outcomes and count the number of tails and heads.
'''

import random

count_heads = 0
count_tails = 0

heads = 1
tails = 0

while True:
	flip = random.randint(0,1)
	if flip == 1:
		count_heads += 1
		print(f'heads: {count_heads}')
	else:
		count_tails += 1
		print(f'tails: {count_tails}')
	ask_flip = input('Do you wish to flip again? (y or no?) ').lower()
	if ask_flip == 'y':
		continue
	else:
		break