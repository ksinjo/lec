from art_high_lower import logo
from data import data
import random 


def format_data(acconut):
    """ Format the account data into printable format  """
    account_name = account_a["name"]
    account_descr = account_a["description"]
    account_country = account_a["country"]
    return (f"{account_name}, a {account_descr}, from {account_country}")

#Display art
print(logo)
#Generate a random Accout from the game data. 
account_a = random.choice(data)
acccount_b = random.choice(data)
if account_a == acccount_b:
    account_b = random.choice(data)

print(f"Compare A:{format_data(account_a)}")
print(f"Compare A:{format_data(account_b)}")

# Format the Acconuit dat int printable format.


# Ask user for a guess.

# Check if user is Correct. 
## Get follwer count of each account 
## Use if statment to check if user is correct. 

# Give user feedback on their guess. 

# Score keeping 

# Make the gaem repeatalbe. 

# Making account at position B become the next account at position 

# Clear the screent between rounds. 