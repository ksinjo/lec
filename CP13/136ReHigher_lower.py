from art_high_lower import logo,vs
from data import data
import random 
from replit import clear

def format_data(acconut):
    """ Format the account data into printable format  """
    account_name = acconut["name"]
    account_descr = acconut["description"]
    account_country = acconut["country"]
    account_follower = acconut["follower_count"]
    return f"{account_name}, a {account_descr}, from {account_country},{account_follower}"

def check_answer(guess,a_follower, b_follower):
    """ Take the user guess and follower counts and returns if tyey got it right."""
    if a_follower > b_follower:
        return guess == "a"
    else:
        return guess == "b"


#Display art
print(logo)
score = 0 
game_should_continue = True
account_b = random.choice(data)

# Make the gmae repeatalbe.
while game_should_continue:
    #Generate a random Accout from the game data. 
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A:{format_data(account_a)}")
    print(vs)
    print(f"Compare B:{format_data(account_b)}")

    # Format the Acconuit dat int printable format.


    # Ask user for a guess.
    guess = input("who has more followers? Type 'A' or 'B' :").lower()

    # Check if user is Correct. 
    ## Get follwer count of each account 
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess,a_follower_count,b_follower_count)

    # Clear the Screen between rounds.
    clear()
    ## Use if statment to check if user is correct. 


    # Give user feedback on their guess. 
    if is_correct:
        score += 1
        print(f"you're right! Current score: {score}" )
    else:
        print(f"sorry,that's wrong. Final score: {score} ")
        game_should_continue = False
# Score keeping 

# Make the gaem repeatalbe. 

# Making account at position B become the next account at position 

# Clear the screent between rounds. 