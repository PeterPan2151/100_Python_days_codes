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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def report(profit_made):
    """Return a formatted string to print the report"""
    return f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g" \
           f"\nMoney: ${profit_made}"


def check_resource(drink_ordered_ingredients):
    """Returns true when order can be made"""
    for item in drink_ordered_ingredients:
        if drink_ordered_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def process_coins():
    """returns the total calculated from coins inserted"""
    print("Pleas insert coins")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.10
    total += int(input("How many nickels? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return total


def transaction_successful(payment_made, drink_cost):
    """return true when payment is accepted"""
    if payment_made >= drink_cost:
        change = round(payment_made - drink_cost, 2)
        print(f"Here is your change: ${change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_drink(choice_drink, ingredients):
    """Deduct the ingredients from the resources"""
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {choice_drink}")


profit = 0
exit_machine = True
while exit_machine:
    user_coffee_choice = input("What would you like? ").lower()
    if user_coffee_choice == 'off':
        exit_machine = False
    elif user_coffee_choice == 'report':
        print(report(profit))
    else:
        drink = MENU[user_coffee_choice]
        if check_resource(drink['ingredients']):
            payment = process_coins()
            if transaction_successful(payment, drink['cost']):
                make_drink(user_coffee_choice, drink['ingredients'])
