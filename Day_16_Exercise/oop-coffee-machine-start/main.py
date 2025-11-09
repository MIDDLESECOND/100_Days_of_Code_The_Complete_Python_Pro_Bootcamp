from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_on = True


while is_on: 
    command = input("What would you like? (espresso/latte/cappuccino/): ")
    if command == "off":
        print("Machine Closed, Bye~")
        is_on = False
    elif command == "report":
        coffee_maker.report()
        money_machine.report()
    elif command in menu.get_items():
        # get the required resource for the order
        ordered_drink = menu.find_drink(command)
        if coffee_maker.is_resource_sufficient(ordered_drink):
            if money_machine.make_payment(ordered_drink.cost):
                coffee_maker.make_coffee(ordered_drink)