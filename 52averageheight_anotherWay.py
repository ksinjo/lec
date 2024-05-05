# Input a Python list of student heights

print("151 145 179")
student_heights = [x for x in input("write input \n").split()]
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇
total_height = 0
for student in student_heights:
  total_height += student

print(total_height)
print(len(student_heights))
print(int((total_height)/len(student_heights)))