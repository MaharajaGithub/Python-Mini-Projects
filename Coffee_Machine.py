######### Coffee Machine Program ##########

# What is this program about ?
# This coffee machine, which is allow user to buy cofee while inputting

# Feautures of this coffee machine :
# Allow user to check the resources left for making a coffee
# Allow user to check the profit the machine made
# Money gets add after every purchase
# Gives back the change

# Starts here :

MENU = {                                                                            # Menu List
    "espresso":{"ingredients":{"water":50,"coffee":18},"cost":100,},
    "latte":{"ingredients":{"water":200,"milk":150,"coffee":24},"cost":150,},
    "cappuccino":{"ingredients":{"water":250,"milk":100,"coffee":24},"cost":200,},
}

profit = 0

resources = {
    "water":1000,
    "milk":1000,
    "coffee":500,
}
print("Welcome to the Tommy - Grace Cofee Making\n")

# is_resource_sufficient() function defines whether there is enough resources to make coffee or not.

def is_resource_sufficient(order_ingredients):
    """ Return True if order can made, False if ingredients are insufficient"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry, there is not enough {item}")
            return False
    return True

# process_coins() function defines how many different types of coins the user inserted.

def process_rupees():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins")
    total = int(input("How many 500?: "))*500
    total += int(input("How many 100? : "))*100
    total += int(input("How many 50?: "))*50
    total += int(input("How many pennies ?: "))
    return total

# is_transaction_successful() function define the transaction

def is_transaction_successful(money_received,drink_cost):
    """Return True when payment is accepted, False if money is insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is your RS{change} change\n")
        global profit
        profit+=drink_cost
        return True
    else:
        print("Sorry the money is insufficient. Money refunded\n")
        return False

# make_coffee() function works after is_transaction_successful() function

def make_coffee(drink_name,order_ingredients):
    """Deduct the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}\n")


is_on = True

while is_on:
    print("Type 'report' to see available resources, Type 'off' to end the machine.")
    print("Espresso: 100rs, Latte: 150rs, Cappuccino: 190rs")
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: RS{profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink['ingredients']):
            payment = process_rupees()
            if is_transaction_successful(payment,drink['cost']):
                make_coffee(choice,drink['ingredients'])
