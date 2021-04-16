"""Blackjack game logic module"""
import bj
import time


"""Imports bj.py to create instances of the following classes: 

    Card, Deck, Hand, Player, Chips 

"""

#Creating a player and a dealer 
bj.clear_screen()
game_table = bj.Table()
player = bj.Player(input(str("Please enter the player's name: ")))
game_on = True



def player_choice(player):
    """Defines a set of choices for players

    """
    choice = 'Invalid Choice'
    while choice.capitalize != ('H' or 'S'):
        choice = str(input('\nHit or Stand? [H/S]: '))
        bj.clear_screen()
        if choice.capitalize() == 'H':
            player.all_cards.append(game_deck.deal_one())
            player.show_all()
            if player.hand_value() == 21:
                print('Blackjack!')
                return False
            elif player.hand_value() > 21:
                print('Player bust')
                return False
            print(f'{player.hand_value()}')
            return True
        elif choice.capitalize() == 'S':
            return False
        elif choice.capitalize() != ('H' or 'S'):
            print(f'{choice}')

while game_on == True:
    
    
    bj.clear_screen()
    game_deck = bj.Deck()
    game_deck.shuffle()
    player.del_cards()
    game_table.del_cards()
    time.sleep(1.5)
    bj.clear_screen()

    #Game logic for dealing initial hand
    for i in range(0,2):
        player.all_cards.append(game_deck.deal_one())    
        game_table.all_cards.append(game_deck.deal_one())

    #Need to display player cards and 1 dealer card
    print(f"{player.name}'s cards: ")
    player.show_all()
    print(f'{player.hand_value()}')
    print(f"\n{game_table.name}'s face up card: ")    
    game_table.show_one()
    
    #Player's Turn
    player_turn = True
    while player_turn == True:
        player_turn = player_choice(player)
    if player.hand_value() > 21:
        
        print(f'{player.name} busts with a hand total of {player.hand_value()}')
        game_on = bj.play_again()
        continue
    elif player.hand_value() == 21:
        print(f'{player.name} wins with a hand total of {player.hand_value()}')
        game_on = bj.play_again()
        continue
        
    #Dealer's Turn
    while game_table.hand_value() < 17:
        game_table.all_cards.append(game_deck.deal_one())
    
    game_table.show_all()
    if game_table.hand_value() > 21:
        print(f'Dealer busts with a hand total of {game_table.hand_value()}')
        #Player automatically wins their bet here
        game_on = bj.play_again()
        continue
    elif game_table.hand_value() == 21:
        print(f'{game_table.name} wins with a hand total of {game_table.hand_value()}')
        game_on = bj.play_again()
        continue
    if player.hand_value() > game_table.hand_value():
        print(f"{player.name} {player.hand_value()} beats {game_table.name} {game_table.hand_value()} !")
        game_on = bj.play_again()
        continue
    elif game_table.hand_value() > player.hand_value():
        print(f"{game_table.name} {game_table.hand_value()} beats {player.name} {player.hand_value()}!")
        game_on = bj.play_again()
        continue
    elif game_table.hand_value() == player.hand_value():
        print('Tie!')
        game_on = bj.play_again()
        continue