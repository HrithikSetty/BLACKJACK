
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':11,'Queen':12,'King':13,'Ace':14}
suits = ('Hearts','Spades','Clubs','Diamonds')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
import random

class Cards:

	def __init__(self,suit,rank):

		self.rank = rank
		self.suit = suit
		self.value = values[rank]

	def __str__(self):
		return self.rank + ' of ' + self.suit

class Deck:

	def __init__(self):

		self.all_cards = []

		for suit in suits:
			for rank in ranks:
				created_card = Cards(suit,rank)
				self.all_cards.append(created_card)

	def Shuffle(self):

		random.shuffle(self.all_cards)

	def Deal_card(self):

		return self.all_cards.pop()

class Players:
	
	def __init__(self,name,balance):

		self.name = name
		self.balance = balance
		self.players_cards = []
	
	def Balance(self,bet):

		self.balance = self.balance - bet

	def Value(self):
		value = 0
		for i in self.players_cards:
			h = i
			value = value + values[h.rank]
		return value

	def __str__(self):

		deck_comp = ''  # start with an empty string
		for card in self.players_cards:
			deck_comp += '\n '+card.__str__() # add each Card object's print string
		return 'The deck has:' + deck_comp
       
          

        
class Dealer:

	money = 1000000000000

	def __init__(self,dealer_cards):

		self.dealer_cards = dealer_cards

	def __str__(self):

		return f'Dealer Card is {self.dealer_cards[0]}\nand a hidden card'

	def Value(self):

		value = 0
		for i in self.dealer_cards:

			value = value + values[i.rank]

playername = input('Welcome to blackjack, Your name: ')
print(f'Hello {playername}')
while True:

	try:
		playerbalance=int(input('How much money do you have: '))
		break
	except:
		print('Asshole')

start = input('Ready to play? : ')


if start[0]=='y' or start[0]=='Y':
	while True:
		new_deck = Deck()
		new_deck.Shuffle
		
		player = Players(playername,playerbalance)
		for j in range(0,2):
			player.players_cards.append(new_deck.Deal_card())
		#player created
		dealer_cards = []
		for k in range(0,2):
			dealer_cards.append(new_deck.Deal_card())
		dealer = Dealer(dealer_cards)
		while True:
			try:
				while True:

					bet = int(input('How much do you wanna bet? : '))
					if bet > player.balance:
						print('Insuficient funds')
					else: 
						print('Bet accepted')
						break
				break
			except:

				print('Asshole')


		print(dealer)
		print(player)
		
		game_on = True
		while game_on:

			a = input('Do you want to hit or stand: ')

			if a[0]=='H' or a[0]=='h':

				player.players_cards.append(new_deck.Deal_card())
				#have to check the value if exceeds 21 or not
				player_cards_value = player.players_cards.Value()
				
				if player_cards_value > 21:

					print('Bust! You suck!')
					dealer.money = dealer.money + bet
					player.balance = player.balance - bet
					game_on = False
					break

				else:
					continue

			elif a[0] == 'S' or a[0] == 's':

				dealer_cards_value = dealer.Value()

				while dealer_cards_value < 17:

					dealer_cards.append(new_deck.Deal_card())
					dealer_cards_value = dealer.Value()

				if dealer_cards_value > 21:

					print(f'{player.name} wins!')
					dealer.money -= bet
					player.balance += bet
					game_on = False
					break

				elif dealer_cards_value > player_cards_value :

					print(f'{palyer.name}, You Suck!')
					dealer.money += bet
					player.balance -= bet
					game_on =False
					break

				elif dealer_cards_value <= player_cards_value:

					print(f'{player.name} wins!')
					dealer.money -= bet
					player.balance += bet
					game_on = False
					break
		d = input('Do you wanna play again: ')
		if d[0]=='Y' or d[0]=='y':
			continue
		else:
			break









			



			

		





