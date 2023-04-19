from replit import clear

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


profit = 0; 
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def process_coins():
    print("Please insert the coins.")
    total = float(input("how many quarters: ")) * 0.25
    total += float(input("how many dimes: ")) * 0.10
    total += float(input("how many nickles: ")) * 0.05
    total += float(input("how many pennies: ")) * 0.01 
    return total


def is_resource_sufficent(order_ingredients):
    """Processes the coins inserted by the user and returns the total amount."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def is_transaction_sucessful(money_received, drink_cost):
    """Checks if the amount of money received is sufficient to buy the drink and returns a boolean value."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Updates the resources and makes the drink."""
    for item in order_ingredients: 
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


def refill(resource_name, amount):
    """Updates the resources and makes the drink."""
    resources[resource_name] += amount

is_on = True

while is_on:
    client_choose = input("What would you like? (espresso/latte/cappuccino): ")

    if client_choose == "off":
        clear()
        print("Até logo ;D")
        is_on = False
        
    
    elif client_choose == "refill":
        refilling = True
        while refilling:
            resource = input("Which resource would you like to refill? (water/milk/coffee): ")
            amount = int(input("How much would you like to add? "))
            refill(resource, amount)
            print(f"{amount}ml of {resource} added to the machine.")
            keep_refill = input("How you like to continue refilling the machine [y/n] ")
            if keep_refill == "y":
                refilling = True
            elif keep_refill == "n":
                refilling = False
            else: 
                refilling = False
    
    elif client_choose == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")

    elif client_choose == "espresso" or client_choose == "latte" or client_choose == "cappuccino":
        drink = MENU[client_choose]
        is_resource_sufficent(drink["ingredients"])
        is_transaction_sucessful(process_coins(), drink["cost"])
        make_coffee(client_choose, drink["ingredients"])

    elif client_choose == "clear":
        clear()
    
    else:
        print("{} não é uma operação válida.".format(client_choose))
        clear()
