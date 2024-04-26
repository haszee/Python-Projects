# BlackJack CODE 1

import random

card_suits = ('Heart', 'Diamonds', 'Spades', 'Clubs')
card_ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
card_values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

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

    def add_cards(self,new_card):
        self.player_cards.append(new_card)

    def __str__(self):
        return f'Player {self.name} has {len(self.player_cards)} cards.'

def calc_sum(card_list):
        # calculate initial sum
        total_value = 0
        for card in card_list:
            total_value += card.value

        # adjust value for Aces
        for card in card_list:
            if card == 'Ace' and total_value > 21:
                total_value -= 10

        return total_value


game_on = True
wins = 0
loss = 0

# player starts with number of chips between 1-100
chips = random.randint(1,100)

# Player can continue playing as long as they have chips
while chips > 0:
    
    # create player
    player_one = Player('P1')
    dealer_one = Player('Dealer')

    # create a new deck & shuffle it
    new_deck = Deck()
    new_deck.shuffle()

    # deal initial 2 cards
    for card in range(2):
        player_one.add_cards(new_deck.deal_one())
        dealer_one.add_cards(new_deck.deal_one())

    print(f'\nPlayer has {chips} chips')

    # player bets a minimum of 1 chip up to maximum equal to number of chips they have
    bet = 1000
    while bet > chips:
        try:
            bet = int(input('\nEnter the number of chips you would like to bet (min: 1, max: your remaining chips): '))
        except ValueError:
            print('\nPlease insert an integer')
    
    print(f'\nPlayer bets {bet} chips.\n')

    continue_game = True

    while continue_game:

        # show players cards
        print(player_one, "\n\nPlayer's cards are:")
        for card in player_one.player_cards:
            print(card)

        # show dealer's 1st card
        print("\nDealer's 1st card: ",dealer_one.player_cards[0])

        # sums up value of cards
        player_sum = calc_sum(player_one.player_cards)
        dealer_sum = calc_sum(dealer_one.player_cards)

        print("\nPlayer's cards' total value: ",player_sum)
        print('Dealer: ',dealer_sum)
        
        # if player's card sum is <= 21 then player can choose to stand or hit
        player_move = input('\nDo you want to stand or hit? ')
        
        if player_move == 'stand':
            
            # show dealer's 2nd card
            print("\nDealer's 2nd card: ",dealer_one.player_cards[1])
            
            # dealer will always hit while their value is <17
            while dealer_sum < 17:
                dealer_one.add_cards(new_deck.deal_one())
                dealer_sum += dealer_one.player_cards[-1].value
                print("\nDealer's new card: ",dealer_one.player_cards[-1])
                print('Dealer: ',dealer_sum)
                
            if player_sum > 21 and dealer_sum > 21: 
                # dealer wins if both go bust
                print('\nBoth Player & Dealer have gone Bust. Dealer has won.')
            elif player_sum > 21 and dealer_sum <= 21: 
                # dealer wins b/c player's value is over 21 & dealer's is <= 21
                loss += 1
                chips -= bet
                print('\nDealer has won.')
                print(f'Player has lost {bet} chips. Player now has {chips} chips.')
            elif dealer_sum > 21 and player_sum <= 21: 
                # player wins b/c dealer's value is over 21 & player's is <= 21
                wins += 1
                chips += bet
                print('\nPlayer has won.')
                print(f'Player has gained {bet} chips. Player now has {chips} chips.')
            elif player_sum <= 21 and dealer_sum <= 21:
                if player_sum == dealer_sum:
                    # tie if both have 21 or some number <21
                    print('\nIt is a tie.')
                elif player_sum > dealer_sum:
                    # player wins if both of their card sums is <21 but player's is higher number
                    # player wins by default if the sum is 21
                    wins += 1
                    chips += bet
                    print('\nPlayer has won.')
                    print(f'Player has gained {bet} chips. Player now has {chips} chips.')
                else:
                    # dealer wins if both of their card sums is <21 but dealer's is higher number
                    # dealer wins by default if the sum is 21
                    loss += 1
                    chips -= bet
                    print('\nDealer has won.')
                    print(f'Player has lost {bet} chips. Player now has {chips} chips.')
            continue_game = False 
        else:
            # if player chooses hit, then deal each of them a card
            player_one.add_cards(new_deck.deal_one())
            
    if chips >= 0:
        if input('\nDo you wish to play again? (y or n?) ').lower() == 'y':
            print('\n'*5)
        else:
            print('\nGame Over!')
            print(f'You won {wins} times. You have ended the game with {chips} chips.')
            print(f'You lost {loss} times. You have ended the game with {chips} chips.')
            break

#----------------------------------------------------------------------------

# BlackJack CODE 2

import random

card_suits = ('Heart', 'Diamonds', 'Spades', 'Clubs')
card_ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
card_values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

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

    def add_cards(self,new_card):
        self.player_cards.append(new_card)

    def __str__(self):
        return f'Player {self.name} has {len(self.player_cards)} cards.'

def calc_sum(card_list):
        # calculate initial sum
        total_value = 0
        for card in card_list:
            total_value += card.value

        # adjust value for Aces
        for card in card_list:
            if card == 'Ace' and total_value > 21:
                total_value -= 10

        return total_value


game_on = True
wins = 0
loss = 0

# player starts with number of chips between 1-100
chips = random.randint(1,100)

# Player can continue playing as long as they have chips
while chips > 0:
    
    # create a new deck & shuffle it
    new_deck = Deck()
    new_deck.shuffle()

    # create player
    player_one = hand('P1')
    dealer_one = Player('Dealer')

    # deal initial 2 cards
    for card in range(2):
        player_one.add_cards(new_deck.deal_one())
        dealer_one.add_cards(new_deck.deal_one())

    print(f'\nPlayer has {chips} chips')

    # player bets a minimum of 1 chip up to maximum equal to number of chips they have
    bet = 1000
    while bet > chips:
        try:
            bet = int(input('\nEnter the number of chips you would like to bet (min: 1, max: your remaining chips): '))
        except ValueError:
            print('Please insert an number')

    
    print(f'\nPlayer bets {bet} chips.\n')

    continue_game = True

    while continue_game:

        # show players cards
        print(player_one, "\n\nPlayer's cards are:")
        for card in player_one.player_cards:
            print(card)

        # show dealer's 1st card
        print("\nDealer's 1st card: ",dealer_one.player_cards[0])

        # sums up value of cards
        player_sum = calc_sum(player_one.player_cards)
        dealer_sum = calc_sum(dealer_one.player_cards)

        print("\nPlayer's cards' total value: ",player_sum)
        print('Dealer: ',dealer_sum)
        
        # if player's card sum is <= 21 then player can choose to stand or hit
        player_move = input('\nDo you want to stand or hit? ')
        
        if player_move == 'stand':
            
            # show dealer's 2nd card
            print("\nDealer's 2nd card: ",dealer_one.player_cards[1])
            
            # dealer will always hit while their value is <17
            while dealer_sum < 17:
                dealer_one.add_cards(new_deck.deal_one())
                dealer_sum += dealer_one.player_cards[-1].value
                print("\nDealer's new card: ",dealer_one.player_cards[-1])
                print('Dealer: ',dealer_sum)
                
            if player_sum > 21 and dealer_sum > 21: 
                # dealer wins if both go bust
                print('\nBoth Player & Dealer have gone Bust. Dealer has won.')
                continue_game = False
            elif player_sum > 21 and dealer_sum <= 21: 
                # dealer wins b/c player's value is over 21 & dealer's is <= 21
                loss += 1
                chips -= bet
                print('\nDealer has won.')
                print(f'Player has lost {bet} chips. Player now has {chips} chips.')
                continue_game = False 
            elif dealer_sum > 21 and player_sum <= 21: 
                # player wins b/c dealer's value is over 21 & player's is <= 21
                wins += 1
                chips += bet
                print('\nPlayer has won.')
                print(f'Player has gained {bet} chips. Player now has {chips} chips.')
                continue_game = False
            elif player_sum <= 21 and dealer_sum <= 21:
                if player_sum == dealer_sum:
                    # tie if both have 21 or some number <21
                    print('\nIt is a tie.')
                    continue_game = False
                elif player_sum > dealer_sum:
                    # player wins if both of their card sums is <21 but player's is higher number
                    # player wins by default if the sum is 21
                    wins += 1
                    chips += bet
                    print('\nPlayer has won.')
                    print(f'Player has gained {bet} chips. Player now has {chips} chips.')
                    continue_game = False
                else:
                    # dealer wins if both of their card sums is <21 but dealer's is higher number
                    # dealer wins by default if the sum is 21
                    loss += 1
                    chips -= bet
                    print('\nDealer has won.')
                    print(f'Player has lost {bet} chips. Player now has {chips} chips.')
                    continue_game = False 
        else:
            # if player chooses hit, then deal each of them a card
            player_one.add_cards(new_deck.deal_one())
            
    if chips >= 0:
        if input('\nDo you wish to play again? (y or n?) ').lower() == 'y':
            print('\n'*5)
        else:
            print('\nGame Over!')
            print(f'You won {wins} times. You have ended the game with {chips} chips.')
            print(f'You lost {loss} times. You have ended the game with {chips} chips.')
            break
