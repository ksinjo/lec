
#Calculator 

#Add
def add(n1, n2):
    return n1 + n2

#Subtract
def subtract(n1, n2):
    return n1 - n2

#Multiply
def multiply(n1, n2):
    return n1 * n2

#Divide
def Divide(n1,n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": Divide
}

# 사용자에게 피연산자1을 입력받게한다.
def calculator():
    num1 = int(input("what's the firstr num :\n"))

    # 딕셔너리 연산자들을 보여준다. 
    for op in operations:
        print(op)
    # 입력받은 심볼을 변수에 저장 
    should_contiune = True
    
    while should_contiune:
        op_symbol = input("Pick an operation")

        num2 = int(input("what's the second num :\n"))
    # 기명성 함수인 calcuation_function 할당 딕셔너리의 키로 접근 
        calulation_function = operations[op_symbol]
    # answer 변수는 위의 함수를 실행(인자1,2 받음)
        answer = calulation_function(num1,num2)
    # printf(f" num1  opertations num2  answer 4개의 인자를 보여준다.  "")
        print(f"{num1} {operations} {num2} = {answer}")
        if input(f"type 'y' to continue calculatin with {answer}: ") == "y":
            num1 = answer
        else: 
            should_contiune=False
            calculator()
# op_symbol = input("Pick an operation from the line above:")
# num3 = int(input("what's the netxt num? :\n"))
# calulation_function = operations[op_symbol]
# second_answer = calulation_function(calulation_function(num1,num2),num3)

# print(f"{first_answer} {operations} {num3} = {second_answer}")