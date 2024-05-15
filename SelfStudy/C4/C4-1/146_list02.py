list_a = [1,2,3]
list_a.extend([11,22,33])
print(list_a)

list_a.append("가")
list_a.append(4)
print(list_a)

list_a.insert(0,"마! 내가 1빠다")
print("최종 출력 :",list_a)