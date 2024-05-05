# Input a Python list of student heights

print("151 145 179")
student_heights = [x for x in input("write input \n").split()]
# Input a Python list of student heights
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
total_height = 0 
for height in student_heights:
  total_height += height
print(f"total height = {total_height}")
# Write your code below this row 👇
number_of_students = 0
for student in student_heights:
  number_of_students += 1
print(f"number of students ={number_of_students}")

average_height = round(total_height/ number_of_students)
print(f"average_height ={average_height}")
 