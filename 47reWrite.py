# 당신 로드킬 당한 동물을 발견해서 묻어주려는 도중에서 
# 30캐럿 다이아몬드를 꿀꺽한 동물이고 주변에서 이 동물 찾고 있습니다. 
# 사채를 숨길 25개의 위치 중에서 Z표시를 할 위치를 설정하세요.

#  숨길 리스트 요소 생성 
l1 = ["⬜️","️⬜️","️⬜️","️⬜️","️⬜️"]
l2 = ["⬜️","⬜️","️⬜️","️⬜️","️⬜️"]
l3 = ["⬜️️","⬜️️","⬜️️","️⬜️","️⬜️"]
l4 = ["⬜️️","⬜️️","⬜️️","️⬜️","️⬜️"]
l5 = ["⬜️️","⬜️️","⬜️️","️⬜️","️⬜️"]
map = [l1,l2,l3,l4,l5]
print("동물을 숨겨라.")
# 숨길 위치 지정 
print("a-e영문과 숫자0~4 조합해서 두개의 문자리터럴 입력 ") 
pos = input()

letter = pos[0].lower()
col= ["a","b","c","d","e"]

letter_index = col.index(letter)
print(f"열의 위치(A,b,c,d,e) : {pos[0]}")
print(f"행의 위치(0, 1,2,3,4 ) :  {pos[1]}")
number_index = int(pos[1])-1

map[number_index] [letter_index] = "Z"
print("당신의 숨긴 구멍의 좌표는 아래와 같습니다.\n")
print(f"{l1}\n,{l2}\n,{l3}\n,{l4}\n,{l5}")



# position = input() # Where do you want to put the treasure?
# # 🚨 Don't change the code above 👆
# # Write your code below this row 👇
# letter = position[0].lower()
# abc=["a","b","c"]
# letter_index = abc.index(letter)
# number_index = int(position[1])-1
# map[number_index] [letter_index] = "X"

# # Write your code above this row 👆
# # 🚨 Don't change the code below 👇
# print(f"{line1}\n{line2}\n{line3}")