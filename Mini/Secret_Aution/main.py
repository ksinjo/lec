# Import packages to clear console
from replit import clear
# Import logo
from intro import logo
# empty dictionary 
bids = {}
# while initial value
bidding_finished = False

# Determination of the highest bidder among secret bidders
def find_highest_bidder(bidding_record):
    # Reset highest bidder value
    highest_bid = 0 
    # String to indicate the highest bidder
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder 
    print(f"The winner is {winner} with a bid of ${highest_bid}")
    print(logo)
# element to repeat
while not bidding_finished:
    name = input("what's you name?:")
    price = int(input("What is your bid?: $"))
    bids[name] = price 
    should_continue = input("are ther any other bidders? Type 'y' or 'n'")
    if should_continue == "n":
        bidding_finished = True 
        find_highest_bidder(bids)
    elif should_continue == "y":
        clear()
