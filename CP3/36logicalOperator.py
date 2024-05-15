print("what's your height")
height = int(input())
bill = 0

if height > 120:
  print("U can ride the rollercoaster")
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
    print("please pay $5")
  elif 12 <= age <= 18:
    bill = 7
    print("please pay $7")
  elif 44 <= age and 55 >= age:
    bill = 0;
    print("free")
  else:
    bill = 9
    print("plase pay $12")

wants_photo = input("Do you want a photo taken? y or n ")
if wants_photo == "y":
  bill += 3 
  print(f"your final bill is {bill}")

else:
    print("sorry, you have to grow taller before you can ride")
    #