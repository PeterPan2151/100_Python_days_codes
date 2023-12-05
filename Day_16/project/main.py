from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
menu = Menu()
coffee_maker = CoffeeMaker()

is_on = True
while is_on:
    options = menu.get_items()
    print(options)
    user_choice = input("What would you like? ").casefold()
    if user_choice == 'off':
        print("Turning off")
        break
    elif user_choice == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(user_choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)

