# if 3 > 2 :
#     a_variable = 10

game_level = 3 
def create_enemy():
    ememies = ["skeleton","zombie","alien"]
    if game_level < 5:
        new_enemy = ememies[0]
    print(new_enemy)