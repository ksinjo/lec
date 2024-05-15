character = {
    "name": "기사",
    "level": 12,
    "items": {
        "sword": "불꽃의 검",
        "armor" : "풀플레이트" 
        },
    "skill": ["베기","세베 베기","아주 세게 베기"]
}
# 실행결과 
#  name : 기사
#  level: 12
#  sword : 불꽃의 검 
#  ammor : 풀플레이트
#  skill : 베기
#  skill : 세게 베기
#  skill : 아주 세게 베기 


for key in character:
# 위 줄까지 제공 
    if type(character[key]) is dict:
        for skey in character[key]:
            print(skey,":", character[key][skey])
    elif type(character[key]) is list:
        for skey in character[key]:
            print(key,":", skey)
    else:
     print(key,":",character[key])