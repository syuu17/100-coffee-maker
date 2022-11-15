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


profit = 0
is_on = True
while is_on:
    current_balance = 0
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
    order = ''
    ingredients = ''
    order_water = 0
    order_milk = 0
    order_coffee = 0
    resource_water = resources["water"]
    resource_milk = resources["milk"]
    resource_coffee = resources["coffee"]
    cost = 0

    while user_input == 'report':
        print(f"Water: {resources['water']}ml \n"
              f"Milk: {resources['milk']}ml \n"
              f"Coffee: {resources['coffee']}g \n"
              f"Profit: ${profit}")
        user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_input == 'espresso' or user_input == 'latte' or user_input == 'cappuccino':
        if user_input == 'latte' or user_input == 'cappuccino':
            order_water = MENU[user_input]['ingredients']["water"]
            order_milk = MENU[user_input]['ingredients']["milk"]
            order_coffee = MENU[user_input]['ingredients']["coffee"]
        else:
            order_water = MENU[user_input]['ingredients']["water"]
            order_coffee = MENU[user_input]['ingredients']["coffee"]
        order = user_input
        ingredients = MENU[user_input]['ingredients']
        cost = MENU[user_input]['cost']
    elif user_input == 'off':
        print("Shutting down.")
        is_on = False
        break
    else:
        print("Please type the exact word next time.")


    def check_resource():
        if order == 'espresso':
            if order_water > resource_water or order_coffee > resource_coffee:
                return False
            else:
                return True
        else:
            if order_water > resource_water or order_coffee > resource_coffee or order_milk > resource_milk:
                return False
            else:
                return True


    def deduct_ingredients():
        if order == 'espresso':
            resources['coffee'] -= order_coffee
            resources['water'] -= order_water
        else:
            resources['coffee'] -= order_coffee
            resources['water'] -= order_water
            resources['milk'] -= order_milk

    def insufficient_resource():
        if not check_resource():
            if order == 'espresso':
                if order_water > resource_water:
                    print("Sorry there is not enough water")
                if order_coffee > resource_coffee:
                    print("Sorry there is not enough coffee")
            else:
                if order_water > resource_water:
                    print("Sorry there is not enough water")
                if order_coffee > resource_coffee:
                    print("Sorry there is not enough coffee")
                if order_milk > resource_milk:
                    print("Sorry there is not enough milk")

    is_sufficient = check_resource()

    def get_coins():
        global current_balance
        print("Please insert coins.")
        quarters = float(input("How many quarters?: ")) * 0.25
        dimes = float(input("How many dimes?: ")) * 0.10
        nickels = float(input("How many nickels?: ")) * 0.05
        pennies = float(input("How many pennies?: ")) * 0.01
        current_balance = quarters + dimes + nickels + pennies
    if is_sufficient:
        deduct_ingredients()
        get_coins()
        if current_balance > cost:
            change = round(current_balance - cost, 2)
            profit += cost
            print(f"Here is ${change} in change. ")
            print("Here is your espresso. Enjoy!")
        else:
            print("Sorry, that's not enough money. Money refunded")
            current_balance = 0
    else:
        insufficient_resource()


