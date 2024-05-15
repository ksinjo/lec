# declear dictionary 
dictionary = {
    "name" : "2020 무긍화",
    "type" : "쉬엄쉬엄 가는 기차",
    "ingredient": ["철","스테인레스강","알루미늄합금","기타 쇳덩이"],
    "origin": "남한"
}

from air import intro
print(intro)

keep_going = True
while keep_going: 
# 사용자로부터 입력 받음
    key = input("> 접근하고자 하는 키:")

    if key in dictionary:
        print(dictionary[key])
    else:
        print("no exist")
    con = input("계속 찾을려면 y,종료 n \n") 
    
    if con == "n":
        keep_going = False
        print("Wash your feet and go to sleep")
    else:
        print("계속 진행됩니다.\n")