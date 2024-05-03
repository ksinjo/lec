# 랜덤룰렛 타겟이름 선정 
#  use for in iterator 
print("Please enter the name of the person you wish to select a rolet for with a space. \n")
names = [x for x in input("Space delimiter data entry \n").split()]
import random
num_items = len(names)
random_choice = random.randint(0,num_items -1) 
target_Animals= names[random_choice]
print(target_Animals + "animals with me")
