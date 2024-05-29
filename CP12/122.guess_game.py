from random import randint
from art3 import logo

print(logo)
# Set difficulty Attempts 
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5 
turns = 0 
# function to check user's guess against actual answer.

def check_answer(guess,answer,turns):
    if guess > answer:
        print("Too high")
        return turns - 1 
    elif guess < answer:
        print("Too low")
        return turns - 1 
    else:
        print(f"You got it! The answer was {answer}")

#Make function to set difficulty.
def set_difficulty():
    level = input("easy or hard or hell 를 입력해서 난이도를 선택해 \n")
    if level == "easy":
        return  EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
# def game()
#choosing a random number between 1 and 100.
def game():
    print("추측게임.. 하 -ㅅ-) 파이썬으로 해 보시게.")
    print(" 1~100 중에서 생성됨.")
    answer = randint(1,100)
    print(f"자네한테만 살짝 알려주는거야.  정답은 말이지 {answer}라네. 믿거나 말거나    ")
    turns = set_difficulty()

    # 게스인풋 전역변수 초기화
    guess = 0
    # 추측값과 실제값 불일치 시 체크함수 반복

    while guess != answer:
        # 남은 시도 횟수 출력 
        print(f"자네가 시도할 수 있는 시도횟수: {turns}")  

    #let the user guess a number.
        guess = int(input("U guess Num:"))
        check_answer(guess,answer,turns)
        turns -= 1 
        if turns == 0 :
            print(f"남은 {turns} 으로 당신은 바보입니다.")
            return
        elif guess != answer:
            print("guess again")

game()

