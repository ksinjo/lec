#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print(" 비밀번호 생성기 온 것을 환영!")
# 문자,기호,숫자 사용자에 입력받음. 
gp_letters = int(input("문자 몇개나 쓸꼬야? \n"))
gp_symbols = int(input("기호는 몇개나 쓸꼬냥? \n"))
gp_number = int(input("숫자는 몇개나 쓸래? \n"))

# 비밀번호를 저장할 빈 문자열 
# easy mode

# password = ""
# #gp_letters = 4
# for char in range(1,gp_letters+1):
#     password_list.append += (random.choice(letters))
#     print(password)

# for char in range(1,gp_symbols+1):
#     password += random.choice(symbols)
#     print(password)

# for char in range(1,gp_number+1):
#     password += random.choice(numbers)

# print(password)

# Hard Level
password_list = []

for char in range(1,gp_letters +1 ) :
    password_list += random.choice(letters)

for char in range(1,gp_symbols +1 ) :
    password_list += random.choice(symbols)

    
for char in range(1,gp_number +1 ) :
    password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char 
print(f"U password is :  {password}")