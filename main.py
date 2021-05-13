from pprint import pprint
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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
   }


def check_resources(order_resourc):
    is_not = True
    for item in order_resourc:
        if order_resourc[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            is_not = False

    return is_not


def process_coins():
    print("Insert coins")
    total = int(input("How many quarters?:")) * 0.25
    total += int(input("How many dimes?:")) * 0.1
    total += int(input("How many nickels?:")) * 0.05
    total += int(input("How many pennies?:")) * 0.01
    return total


def transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is {change}$")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False


def make_cofe(drink_name, order_resours):
    for item in order_resours:
        resources[item] -= order_resours[item]
    print(f"It's you {drink_name}☕. Enjoy")

is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino) ")
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}ml")
        print(f"Money: {profit}$")
    else:
        drink = MENU[choice]
        if check_resources(drink["ingredients"]):
            payments = process_coins()
            if transaction_successful(payments, drink["cost"]):
                make_cofe(choice, drink["ingredients"])

