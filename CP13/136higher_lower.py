#로고를 보여준다.
# Compare A : 
# vs 아스키 출력
# Aginst B : 출력 
# Who has more follwers? type 'a' or 'b': 

from data import data
from random import randint
from art_high_lower import logo
from art_high_lower import vs
print(logo)


a = randint(0,49)
b = randint(0,49)

        # 'name': 'Instagram',
        # 'follower_count': 346,
        # 'description': 'Social media platform',
        # 'country': 'United States'

def compare(a):
    print(f"Comare A: {data[a]["name"]},a {data[a]["description"]},from {data[a]["country"]}")

def aginst(b):
    print(f"Against B: {data[b]["name"]},a {data[b]["description"]},from {data[b]["country"]}")

def eval(a,b):
    if data[a]["follower_count"] >  data[b]["follower_count"]:
        return "a"
    else:
        return "b"
# confirm answer 
print(f" a : {data[a]['follower_count']} b:  {data[b]['follower_count']}")

game_contiune = True
while game_contiune:
    compare(a)
    print(vs)
    aginst(b)
    type = input("Who has more follwers? Type 'a' or 'b': ")
    answer = eval(a,b)
    # print(eval(a,b))

    
    if type ==  answer:
        score= 0 
        score += 10
        print(f"U right! Current score:{score}")
        
    else:
        game_contiune = False
        print(f"sorry. u score:{score}")

