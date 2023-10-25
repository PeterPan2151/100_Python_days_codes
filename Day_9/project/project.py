import art
import os


def highest_bidder(bid_record):
    score = 0
    for bidder in bid_record:
        bidder_score = bid_record[bidder]
        if bidder_score > score:
            score = bidder_score
            current_winner = bidder
    print(f"The winner is {current_winner} with a bid of ${score}")


print(art.logo)
bidders = {}
game_on = True

while game_on:
    name = input("Enter the bidders name: ")
    bid_price = float(input("Enter bidding price: "))

    bidders[name] = bid_price
    more_bidders = input("Are there any more bidders? 'yes' or 'no'? ").lower()
    if more_bidders == 'no':
        game_on = False
        highest_bidder(bidders)
    elif more_bidders == 'yes':
        os.system('cls')
        pass
    else:
        print("invalid choice.")
