print("This is a love calculator. What is your score with the opposite sex, pets, or unfamiliar animals you like? (Dugudugu~)")
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
    print(f"Your love score is {love_score}.")
elif (love_score >= 1)  and (love_score <= 30):
    print(f"Don't love me. The score of eternal unrequited love and forbidden love is {love_score}.")
elif (love_score >= 30)  and (love_score <= 50):
    print(f"Love-hate relationship... What about the score? It is {love_score}.")

elif (love_score >= 50)  and (love_score <= 70):
    print(f"When one of the two is satisfied, my score is {love_score} .")

elif (love_score >= 70)  and (love_score <= 89):
    print(f" love partner  {love_score} .")    

else:
    print(f" U'are my destiny  {love_score} .")
    #