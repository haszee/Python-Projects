import random

card_suits = ('Heart', 'Diamonds', 'Spades', 'Clubs')
card_ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
card_values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card():

	# Suit, Rank, Value for suits
	def __init__(self,suit,rank):
		self.suit = suit
		self.rank = rank
		self.value = card_values[rank]

	def __str__(self):
		return self.rank + " of " + self.suit

class Deck():

	def __init__(self):
		# create new deck
		self.card_deck = []
		for suit in card_suits: # goes through all the suits
			for rank in card_ranks: # goes through all the cards in each suit
				self.card_deck.append(Card(suit,rank))

	def shuffle(self):
		random.shuffle(self.card_deck)

	def deal_one(self):
		return self.card_deck.pop()

class Player():
	def __init__(self,name):
		self.name = name
		self.player_cards = []

	def remove_one(self):
		return self.player_cards.pop(0)

	def add_cards(self,new_cards):
		if type(new_cards) == type([]):
			# for multiple new cards, a list is created
			# this list is then added to the end of original list
			# extend adds the objects in the list as individual objects
			# append would have added the objects as one single object thereby creating a nested list
			self.player_cards.extend(new_cards)
		else:
			self.player_cards.append(new_cards)

	def __str__(self):
		return f'Player {self.name} has {len(self.player_cards)} cards.'

# create players
player_one = Player('P1')
player_two = Player('P2')

# create a new deck & shuffle it
new_deck = Deck()
new_deck.shuffle()

# split the deck & give each player 26 cards
for card in range(int(len(new_deck.card_deck)/2)):
	player_one.add_cards(new_deck.deal_one())
	player_two.add_cards(new_deck.deal_one())

game_on = True
round_num = 0

while game_on:
	round_num += 1

	print(f'Round {round_num}') 

	if len(player_one.player_cards) == 0:
		print('Player 1 is out of cards! Game Over!\nPlayer 2 wins!')
		#game_on = False
		break
	elif len(player_two.player_cards) == 0:
		print('Player 2 is out of cards! Game Over!\nPlayer 1 wins!')
		#game_on = False
		break

	# these are the cards on the table
	player_one_table = []
	player_one_table.append(player_one.remove_one())
	
	player_two_table = []
	player_two_table.append(player_two.remove_one())

	at_war = True

	while at_war:
		if player_one_table[-1].value > player_two_table[-1].value:
			player_one.add_cards(player_one_table)
			player_one.add_cards(player_two_table)

			# no longer at war
			at_war = False

		elif player_one_table[-1].value < player_two_table[-1].value:
			player_two.add_cards(player_one_table)
			player_two.add_cards(player_two_table)

			# no longer at war
			at_war = False

		else:
			print('WAR!')
			# check to see if player has the 5 cards required to offer
			if len(player_one.player_cards) < 5:
				print("Player 1 unable to play war! Game Over at War")
				print("Player 2 Wins! Player 1 Loses!")
				# game_on = False
				break
			elif len(player_two.player_cards) < 5:
				print("Player 2 unable to play war! Game Over at War")
				print("Player 2 Wins! Player 1 Loses!")
				# game_on = False
				break
			else:
				for num in range(5):
					player_one_table.append(player_one.remove_one())
					player_two_table.append(player_two.remove_one())

