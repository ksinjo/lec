# 구현 사항 
# 사용자의 최대 입력을 받는다. 
# 최대 값은 1000까지로 제한
# 최대값이 100 경계로 가중치를 두어 IQ 최대 점수를 상승 
# 시도횟수 차감에 따라 -10 
# 

# 1 랜덤 숫자 만들기
from random import randint
from arts import logo
from arts import cat
# 난이도 시도 횟수 
EASY_TURNS = 10
NOMAL_TURNS = 7
HARD_TURNS = 5
EXTREAM_TURNS = 3 

# 사용자의 max 값을 받아 랜덤 값 생성 
print(logo)



def check_answer(guess,value,turns): # turns 인자로 넘김
    if guess > value:
        print(f"현재 맞췄다면 너의 IQ는 {D_IQ}!  입력 값보다 높음")
        turns -= 1  # /// 누락 check_answer 실행되면 시도 횟수 감소 
    elif guess < value:
        print(f"현재 맞췄다면 너의 IQ는 {D_IQ}!  입력 값보다 낮음")
        turns -= 1 
    else:
        print(f"정답! 너의 IQ :{D_IQ} 추카 추카 ")
        print(dog)
        
    
# 유저가 선택한 난이도에 따른 시도횟수 
def set_difficulty():
    level = input("Selectable Difficulty Level: 'easy','normal','hard','extream' ")
    if level == "easy":
        return EASY_TURNS
    elif level =="noraml":
        return NOMAL_TURNS
    elif level == "hard":
        return HARD_TURNS
    else:
        return EXTREAM_TURNS

print("추측 게임에 온 걸 환영한다. 잡종!")
u_num = int(input("1~1000 중에서 원하는 숫자를 입력하세요 \n"))

value = randint(1,u_num)
print(f"니가 입력한 최대값 {u_num} 정답: {value}" )


D_IQ = 150
if value > 201:
    D_IQ = 155
elif value > 301:
    D_IQ = 160
elif value > 401:
    D_IQ = 165
elif value > 501:
    D_IQ = 170
elif value > 601:
    D_IQ = 175
elif value > 701:
    D_IQ = 180
elif value > 801:
    D_IQ = 185
elif value > 901:
    D_IQ = 190
else:
    D_IQ = 190

def game():

    turns = set_difficulty()
    guess = 0 
    while guess != value:
        print(f"너님 남은 시도횟수 : {turns}")
        guess=int(input("니가 추측한 수를 입력해 \n"))
        check_answer(guess,value,turns)
        turns -=1
        if turns ==0:
            print(f"당신은 머리는 돌 수준입니다. 내구성만큼은 뛰어납니다.")
            return
        elif guess != value:
            print(cat)
            print("당신님에게 한번 더 기회를 선사하마! 잘 찍어라")
            
game()

# 게임시작과 종료 매커니즘 - 구현 
# 사용자 입력받은 최대 값을 기준으로 랜덤 값 지정하기 - 구현 
# 추가 난이도 - 구현 
# 시도횟수에 따라 지능 점수  - 구현
# 지능점수에 따른 이미지 출력 - 1개만 만듬. 시간낭비

