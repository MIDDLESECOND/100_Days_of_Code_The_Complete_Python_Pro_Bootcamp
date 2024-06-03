MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    "money": 0
}


def is_resource_efficient(ordered_ingredients):
    for item in ordered_ingredients:
        # check if resource is enough for whatever drink chosen
        #  and if not enough and print 'Sorry there is not enough water.'
        if ordered_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def coffee_machine():
    global MENU, resources
    # input “ What would you like? (espresso/latte/cappuccino): ”
    coffee_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # add a secret function "off" to turn off the machine
    if coffee_input == "off":
        print("Machine Closed, Bye~")
    # if "report" is inputted , show report of all current values
    elif coffee_input == "report":
        print(f"Water: {resources["water"]}ml")
        print(f"Milk: {resources["milk"]}ml")
        print(f"Coffee: {resources["coffee"]}g")
        print(f"Money: ${resources["money"]}")
        # reshow this everytime time action is completed.
        coffee_machine()

    elif coffee_input in ("espresso", "latte", "cappuccino"):
        ordered_ingredients = MENU[coffee_input]["ingredients"]
        if is_resource_efficient(ordered_ingredients):
            print("Please insert coins")
            num_of_quarters = int(input("How many quarters?: "))
            num_of_dimes = int(input("How many dimes?: "))
            num_of_nickles = int(input("How many nickles?: "))
            num_of_pennies = int(input("How many pennies?: "))
            # if remaining resource is enough, prompt the coins to be inserted, calculate inserted amount
            inserted_amount = (num_of_quarters * 0.25 + num_of_dimes * 0.1 +
                               num_of_nickles * 0.05 + num_of_pennies * 0.01)
            coffee_cost = MENU[coffee_input]["cost"]
            if inserted_amount >= coffee_cost:
                # add the inserted value to profit and offer changes rounded to 2 decimal places
                resources["money"] += coffee_cost
                change = round((inserted_amount - coffee_cost), 2)
                print(f"Here is ${change} in change.")
                # deduct the resource to make the drink and tell the user f“Here is your {drink}. Enjoy!”.
                for item in ordered_ingredients:
                    resources[item] -= ordered_ingredients[item]
                print(f"Here is your {coffee_input} ☕. Enjoy!")
            else:
                # check if inserted coins value is enough, if not, print 'Sorry that's not enough money. Money
                # refunded.'
                print("Sorry that's not enough money. Money refunded.")

        # reshow this everytime time action is completed.
        coffee_machine()


coffee_machine()
