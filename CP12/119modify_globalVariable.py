# global variable 
mario_life = 3

# def 
def increase_life():
    print(f"cur life : {mario_life}")  
    return mario_life + 1  # retur 

mario_life = increase_life() 
print(f"버섯을 먹은 자네의 생명 수 : {mario_life} ")


# enemies = 10

# def increase_enemise():
#     # global enemies
#     # enemies += 1 
#     print(f"ememies inside function : {enemies}")
#     return enemies + 1 

# enemies = increatse_enemise()
# print(f"ememies outside function :{enemies}")