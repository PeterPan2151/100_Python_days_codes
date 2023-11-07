import random


def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """This function calculates the sum of the cards in a list"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "DRAW"
    elif computer_score == 0:
        return "LOOSE TO A BLACKJACK"
    elif user_score == 0:
        return "WON WITH A BLACKJACK"
    elif user_score > 21:
        return "YOU WENT OVER YOU LOOSE"
    elif computer_score > 21:
        return "COMPUTER WENT OVER, YOU WIN"
    elif user_score > computer_score:
        return "YOU WIN"
    else:
        return "YOU LOOSE"


def game():
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_deal = input(
                "Type 'y' to get another card, type 'n' to pass: ")
            if user_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards} and final score is: {user_score}")
    print(
        f"Computer's final hand: {computer_cards} and final score is: {computer_score}")
    compare(user_score, computer_score)


while input("Do you want to play a game of Blackjack? Type 'y' or 'n':") == 'y':
    game()
