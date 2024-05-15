# declear dictionary 
dictionary = {
    "name" : "2020 무긍화",
    "type" : "쉬엄쉬엄 가는 기차",
    "ingredient": ["철","스테인레스강","알루미늄합금","기타 쇳덩이"],
    "origin": "남한"
}

value = dictionary.get("존재하지 않는 키")
print("값:",value)

#None 확인 방법
if value == None:
    print("존재하지 않는 키에 접근함")