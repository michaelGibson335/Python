#dictionary containing the cofee machine menu to choose from
#expresso, latte, cappuccino 

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

#dictionary containing amount of ingredients available to make coffee
#profit variable to hold monetary value gain for the machine 
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

#function taking order_ingredients from drink variable pointing to MENU
#loop through items in order ingredients
#test to see if order_ingredients item is greater than or equal to starting resources items
#if greater than, return false
#else return true
def is_resources_sufficient(order_ingredients):
    is_enough = True
    for item in order_ingredients: 
        if order_ingredients[item] >= resources[item]:
            print(f'Sorry there is not enough {item}. ')
            is_enough = False
    return is_enough

#function to process coins for quarters, nickels, dimes and pennies
#increment total by how many coins they put in 
def process_coins():
    print('Please insert coins. ')
    total = int(input('How many quarters?: ')) * 0.25
    total += int(input('How many dimes?: ')) * 0.1
    total += int(input('How many nickels?: ')) * 0.05
    total += int(input('How many pennies?: ')) * 0.01
    return total

#return true if money is accepted, else return false if funds are insufficient
#if true, profit gets incremented
#also track leftover change and return change
def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f'Here is ${change} in change')
        global profit 
        profit += drink_cost
        return True
    else:
        print("Insufficent funds, money refunded")
        return False

#deduct ingredents used from machine resources when dispensing coffee         
def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}")

#prompt user to input what type of coffee they'd like
#prompt should show everytime the action has been completed as well, place in while loop
#also, coffee machine needs option to turn off

#variable to check condition if it is on
#if user inputs 'off' in while loop prompt
#it changes is_on to False and stops the while loop below
#if input is 'report', it will report coffee resources dictionary contents
is_on = True

while is_on:
    coffeeChoice = input('What would you like? (expresso/latte/cappuccino): ')
    if coffeeChoice == 'off':
        is_on = False
    elif coffeeChoice == 'report':
        print(f'Water: {resources["water"]}ml')
        print(f'Milk: {resources["milk"]}ml')
        print(f'Coffee: {resources["coffee"]}g') 
        print(f'Money: ${profit}')
    else:
        drink = MENU[coffeeChoice]
        if is_resources_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(coffeeChoice, drink['ingredients'])

