pets = [
    {"name" : "구름" ,"age" : 5},
    {"name" : "초코" ,"age" : 3},
    {"name" : "아지" ,"age" : 3},
    {"name" : "호랑이" ,"age" : 1}
    
]

print("# 우리 동네 애완 동물들")
# 리스트 내에서 딕셔너리 접근 
# 아래코드처럼 수동으로 접근하면 피곤해짐. 
# print(f"{pets[0]["name"]},{pets[0]["age"]}살")

print(len(pets))
last_len = len(pets)
i = 0
for i in range(i, last_len):
    print(f"{pets[i]["name"]} {pets[i]["age"]}살")
    i+=1


# for pet in pets:
#     print(pet[0]["name"])