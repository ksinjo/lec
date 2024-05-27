from random import randint
from art3 import logo

print(logo)
# Set difficulty Attempts 
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5 

# function to check user's guess against actual answer.
def check_answer(guess,answer):
    if guess > answer:
        print("Too high")
    elif guess < answer:
        print("Too low")
    else:
        print(f"You got it! The answer was {answer}")

#Make function to set difficulty.
def set_difficulty():
    level = input("easy or hard or hell 를 입력해서 난이도를 선택해 \n")
    if level == "easy":
        return  EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

#choosing a random number between 1 and 100.
print("추측게임.. 하 -ㅅ-) 파이썬으로 해 보시게.")
print(" 1~100 중에서 생성됨.")
answer = randint(1,100)
print(f"자네한테만 살짝 알려주는거야.  정답은 말이지 {answer}라네. 믿거나 말거나    ")
turns = set_difficulty()
print(f"자네가 시도할 수 있는 시도횟수: {turns}")

#let the user guess a number.
guess = int(input("U guess Num:"))
check_answer(guess,answer)
