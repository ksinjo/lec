#Calculator
def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}
from art import logo
def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True # while문 반복 초기값

    while should_continue: # while문 스코어범위 들여쓰기
        operation_symbol = input("Pick an operation: ") 
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f" type 'y'to continye calculating wiht {answer}, or type 'n' to exit.: ") =="y":
            num1= answer 
        else:
            should_continue = False
            calculator() 
       
calculator() # 재귀적함수 호출 
#Here we select "*" which overides the "+" we selected on line 26.

