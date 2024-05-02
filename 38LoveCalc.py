print("사랑계산기입니다. 당신이 좋아하는 이성또는 애완동물 및 낯선 동물과의 점수는!! (두구두구~)")
Uname = input() 
Target_name = input()

combined_names = Uname + Target_name 
lower_names = combined_names.lower() 

t = lower_names.count("t")
u = lower_names.count("u")
r = lower_names.count("r")
e = lower_names.count("e")

f_digit = t + u + r + e 

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")

s_digit = l + o + v + e 

love_score = int(str(f_digit) + str(s_digit))

if (love_score <10) or (love_score >90) : 
    print(f"당신의 사랑의 점수는 {love_score} 입니다.")
elif (love_score >= 1)  and (love_score <= 30):
    print(f"사랑하지 마요. 영원한 짝사랑 금지된 사랑의 점수는 {love_score} 입니다.")
elif (love_score >= 30)  and (love_score <= 50):
    print(f" first는 아니지만 second or Third 이성친구 가능 제 점수는 {love_score} 입니다.")

elif (love_score >= 50)  and (love_score <= 70):
    print(f" 둘중 하나가 꽃힌 상태 자 제 점수는용 {love_score} .")

elif (love_score >= 70)  and (love_score <= 89):
    print(f" 우리 동거까지 생각했어~ 제 점수는 요요요 {love_score} .")    

else:
    print(f"우리 결혼까지 생각했어요.   {love_score} 되나봄.")
    #