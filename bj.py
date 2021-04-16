'''bj.py'''

#Python module for blackjack base game logic

import random
import time
import os

suits = ('Clubs','Spades','Diamonds','Hearts')

ranks = (
    'Two','Three','Four','Five','Six','Seven',
    'Eight','Nine','Ten','Jack','Queen','King','Ace'
    )

values = {
    'Two':2, 'Three':3,'Four':4,'Five':5,
    'Six':6,'Seven':7,'Eight':8,'Nine':9,
    'Ten':10,'Jack':10,'Queen':10,'King':10,'Ace':1
    }

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def play_again():
    """Decide whether or not to continue playing


    """
    choice = 'k'
    while choice.capitalize() != ('Y' or 'N'):
        choice = str(input('Play again? [Y/N]: '))
        if choice.capitalize() == 'Y':
            return True
        elif choice.capitalize() == 'N':
            clear_screen()
            print('Thanks for playing!')
            time.sleep(1.5)
            clear_screen()
            return False
        else:
            print('Please choose Y or N')    

class Card():
    
    """Creates a card object with rank, suit, and value.
    
    Contains a string method to easily see the suit and rank of card
    """
    
    def __init__(self,rank,suit):
        """Constructor assigns suit, rank, and value attributes"""
        self.suit = suit
        self.rank = rank
        self.value = values[rank] #References the values dictionary
        
    def __str__(self):
        """Returns the string 'Rank of Suit' when printed"""
        return self.rank + " of " + self.suit

class Deck():
    
    """Creates an empty list then fills it with cards
    
    __init__ method iterates through the suits and ranks to generate 
    a list of 52 playing cards. 
    shuffle method randomizes the order cards appear in the list
    deal_one method returns the first card in the deck list
    for simplicity's sake, a new game deck will be created for each blackjack hand,
    and the player's cards will simply be discarded
    """
    def __init__(self): 
        """Iterates through suit and rank list to form 52 card deck"""
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                created_card = Card(rank,suit)
                self.all_cards.append(created_card)
                
    def shuffle(self):
        """Uses the random method from random library to shuffle deck"""
        random.shuffle(self.all_cards)
        print('The deck has been shuffled.')    

    def deal_one(self):
        """Removes card at deck index zero and returns it as output"""
        return self.all_cards.pop(0)


class Hand(): 
    """ Base class. Holds cards objects in a list for players
    
    Methods include:
    Compute hand value
    Accept new cards
    Empty hand
    """
    
    def __init__(self):
        """Creates an empty list to serve as the hand"""
        self.all_cards = []
        
    def recieve_card(self,dealt_card):#Is this method irrelevant?
        ''' Adds a new card to the hand list
        
        Recieve card method accepts a card object as a parameter
        The Card is then appended to the hand list
        '''
        self.all_cards.append(dealt_card)
        print('There are now {} cards in hand.'.format(len(self.all_cards)))

    def return_card(self):
        """Places cards in hand into a list and returns the list """
        discard = []
        for card in self.all_cards:
            discard.append(self.all_cards.pop())

        return discard    

 
    def show_one(self):
        """Prints the rank and suit of the first card in hand."""
        
        print(self.all_cards[0])

    def show_all(self):
        """Prints the rank and suit of all cards in hand."""

        for card in self.all_cards:
            print(card)
        
    def hand_value(self):
        '''Computes the value of the cards in hand
        
        xChecks the rank of the card against its value in the dictionary
        Checks to see if the value is greater than 21
        If the value is greater than 21, checks to see if there is an ace in hand
        If the value is greater than 21 and there is an ace, the value of the ace becomes 1
        This is factored into the new value
        Value is then returned as the output of the method.
        '''
        value = 0
        for i in self.all_cards:
            value += values[i.rank]
        return value

class Player(Hand):  
    #Might be worth it to split player and dealer into 2 distinct classes that inherit from Hand and Chips
    """Representation of computer or human blackjack players, as well as the Dealer
    
    Player class inherits the Hand class methods and attributes to simplify value comparisons
    Player class also inherits the Chips class.    
    """
    
    def __init__(self,name):
        """Calls __init__ to create instances of hand and chips for each player. 
        
        Also asks the player for their name and forces it to be a string
        """
        Hand.__init__(self)
        #Chips.__init__(self) ------------------Still need to add this class.
        self.name = str(name)
        print(f'Welcome to the table, {self.name}.')

    def card_count(self):
    	self.count = str(len(self.all_cards))
    	return f"{self.name} has {self.count} cards."

    def del_cards(self):
        del self.all_cards[0::]
        print(f"{self.name}'s hand is empty")
    def __str__(self):
    	return self.name

class Chips():
    """Representation of player bank values. """
    
    def __init__(self):
        pass

class Table(Player):
    """The Game Table
    
    Creates an instance of the Player class that serves as the dealer. 
    
    """

    def __init__(self):
        """Instantiates a table and a dealer for that table"""
        
        print('The blackjack table is now ready for play.')
        Player.__init__(self,'Dealer')
    pass

    
