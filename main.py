__author__ = "John McCrimmon"
__version__ = "1.0.1"

from inventory import MENU, resources


def prompt_menu():
    """Prompts user with the available choices and allows the user to enter their drink. 'Report' will generate a
    report of what resources are in the coffee machine and 'off' will end the program."""
    menu_selection = input("\nWhat would you like? (espresso/latte/cappuccino): ")
    return menu_selection.lower()


def print_report():
    """Prints a list of the current values for the resources in the coffee machine."""
    print(f"\nREPORT\nWater: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\n"
          f"Money: ${resources['money']}")


def can_drink_be_made(drink):
    """Checks to see if the resources in machine are capable to make the drink. If there is not enough of one
    ingredient then it will return the first missing ingredient as a string. Otherwise, it will return 'yes' implying
    that there are enough resources to make the selected drink."""
    if resources["water"] < MENU[drink]["ingredients"]["water"]:
        return "Water"
    elif resources["milk"] < MENU[drink]["ingredients"]["milk"]:
        return "Milk"
    elif resources["coffee"] < MENU[drink]["ingredients"]["coffee"]:
        return "Coffee"
    else:
        return "yes"


def insert_coins():
    """Prompts user to insert coins, allows user to input how many of each coin they are inputting in the machine.
    Calculates the total value of coins inputted and returns a rounded value."""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    total = round(total, 2)
    print(f"Money inserted: ${total}")
    return total


def make_drink(drink):
    """Processes how much of each resource is being used based on what drink was ordered."""
    print(f"Making {drink}...")
    resources["water"] -= MENU[drink]["ingredients"]["water"]
    resources["milk"] -= MENU[drink]["ingredients"]["milk"]
    resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]


# Drives coffee machine
is_on = True
while is_on:
    choice = prompt_menu()
    if choice == "report":
        print_report()
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        if can_drink_be_made(choice) == "yes":
            user_money = insert_coins()
            if user_money >= MENU[choice]["cost"]:
                # Adds the price of drink to machines total money in machine
                resources["money"] += MENU[choice]["cost"]
                # Gives difference of user's inserted money back to the user
                print(f"Here is ${round(user_money - MENU[choice]['cost'], 2)}")
                make_drink(choice)
                print(f"Here is your {choice}. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            print(f"Sorry there is not enough {can_drink_be_made(choice)}.")
    elif choice == "off":
        print("Machine turning off...")
        is_on = False
    else:
        print("Please enter a valid selection.")
