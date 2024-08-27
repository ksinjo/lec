MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0 # 수익을 나타내는 변수 추가 
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_sufficient(order_ingredients):
    """Returns ture when order can be made, False if ingrdents are insufficient"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
           print(f"sorry there is not enough {item}") 
           return False
    return True     

def make_coffee(drink_name,order_ingredient):
    """ Debuct the required ingredients from the resources"""
    for item in order_ingredient:
        resources[item] -= order_ingredient[item]
        print(f" Here is your {drink_name}")



def process_coins():
    """ Returns the total calculated from coins inserted """
    print("please insert coins")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many quarters?: ")) * 0.1
    total += int(input("how many quarters?: ")) * 0.05
    total += int(input("how many quarters?: ")) * 0.01
    return total 


def is_transaction_successful(money_recived, drink_cost):
    """ Return True when the payment is accepted, or false if money is insufficient"""
    if money_recived >= drink_cost:
        change = round(money_recived - drink_cost, 2)
        print(f"Here is #{change} in change")
        global profit
        profit += drink_cost
        return True
    else:

        print("sorry that's not enought money. Money refunded")
        return False
        

is_on = True
while is_on:
    choice = input("what would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False 
    elif choice == "report":
        print(f"resources Water:{resources["water"]}ml")
        print(f"resources milk:{resources["milk"]} ml")
        print(f"resources coffee:{resources["coffee"]} ml")
        print(f" Money: {profit}")
    else: 
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment,drink["cost"]):
                make_coffee(choice,drink["ingredients"])