import random
import os
from art import logo


def clear_console():
  os.system('cls')
  
  
def deal_card(cards_list):
    """Returns a random card from the deck"""
    card = random.choice(cards_list)
    return card


def calculate_score(player_list_cards):
    """This function calculates the sum of the cards in a list"""
    if sum(player_list_cards) == 21 and len(player_list_cards) == 2:
        return 0
    
    if 11 in player_list_cards and sum(player_list_cards) > 21:
        player_list_cards.remove(11)
        player_list_cards.append(1)
        
    return sum(player_list_cards)


def compare(users_score, computers_score):
    if users_score == computers_score:
        return "Its a TIE"
    elif computers_score == 0:
        return "YOU LOOSE, COMPUTER HAS BLACKJACK"
    elif users_score == 0:
        return "YOU WIN, WITH BLACKJACK"
    elif users_score > 21:
        return "OVER 21 YOU LOOSE"
    elif computers_score > 21:
        return "COMPUTER OVER 21 YOU WIN"
    elif users_score > computers_score:
        return "YOU WIN HIGHEST SCORE"
    else:
        return "YOU LOOSE LOWEST SCORE"
    
    
def game():
    print(logo)
    user_cards = []
    computer_cards = []    
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    game_on = False

    for _ in range(2):
        user_cards.append(deal_card(cards))
        computer_cards.append(deal_card(cards))



    while not game_on:
        player_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
    
        print("Players cards: ")
        print(user_cards)
        print()
        print("Computer's card: ")
        print(computer_cards[0])
        print()
        print(f"player score {player_score}")
    
        if player_score == 0 or computer_score == 0 or player_score > 21:
            game_on = True
        else:
            user_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            print()
            if user_deal == 'y':
                user_cards.append(deal_card(cards))
            else:
                game_on = True 
        
            
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card(cards))
        computer_score = calculate_score(computer_cards)
        
        
    print(f"Your final hand: {user_cards} and final score is: {player_score}\n")
    print(f"Computer's final hand: {computer_cards} and final score is: {computer_score}\n")
    print(compare(player_score, computer_score))
    
    
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    clear_console()
    game()

