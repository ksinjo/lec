from art import logo
from game_data import data
import random
#display art 

def format_data(account):
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return (f"{account_name}, a {account_descr}, from {account_country}")


print(logo)

# Generate a random account from the game data.
# 게임 데이터에서 랜덤하게 자겨와서 생성
account_a = random.choice(data)
account_b = random.choice(data)
if account_a == account_b:
    account_b = random.choice(data)

print(f"Compare A: {format_data(account_a)}")
print(f"Compare B`: {format_data(account_b)}")

# Format account data into printable format.
# 데이터를 정렬해서 출력하는 방법  data의 리스트 내에 딕셔너리 정렬해서 출력할 방법 


# Ask user for a guess.

# Check if user is correct. 유저가 정답이 맞는지를 체크
## Get follower count. 팔로워 수를 가져온다 
## If Statement  조건문

# Feedback.

# Score Keeping.

# Make game repeatable.

# Make B become the next A.

# Add art.

# Clear screen between rounds.