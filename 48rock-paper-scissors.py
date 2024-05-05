rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images= [rock,paper,scissors]
import random



user_choice = int(input("0 = rock , 1 = paper 12 = Scissors. What Do U Choose?"))
if user_choice >= 3 or user_choice < 0:
    print("U type an invalid number, U lose")
else:
    print("This is a valid value.")
        
    print(f"My choice is \n {game_images[user_choice]}")

    com_choice = random.randint(0,2)
    print(f"com choice \n {game_images[com_choice]}")

    # print(f"{user_choice}\n")
    # print(f"{com_choice}\n")



    if user_choice == 0 and com_choice ==2:
        print("U win")
    elif com_choice == 0 and user_choice == 2:
        print("U lose")

    elif user_choice < com_choice : 
        print("U lose!")

    elif com_choice > user_choice :
        print("U win")    
    elif user_choice == com_choice :
        print("it's a draw")
    elif user_choice >=3 or user_choice < 0 :
        print("you typed an invalid number, you lose!")