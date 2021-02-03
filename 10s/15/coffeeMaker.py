from menu import MENU, resources

profit = 0
# To Do: 1. Print report of all coffee machine resources
def report():
    print("Available Resources\n*******************")
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}\n*******************")
    print(f"Profit: {profit}\n")
# To Do: 2. Check resources sufficient to make drink order
def is_sufficient_resources (order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, not enough {item}.")
            return False
    return True
# To Do: 3. process coins for sale
def process_coins():
    print("Please insert coins:\n")
    total = float(input("Insert number of quarters:\n"))*0.25
    total += float(input("Insert number of dimes:\n"))*0.10
    total += float(input("Insert number of nickels:\n"))*0.05
    total += float(input("Insert number of pennies:\n"))*0.01
    return total
# To Do: 4. check for successfull transaction
def is_transaction_successful(drink_cost, money_received):
    if drink_cost >= money_received:
        change = round(drink_cost - money_received, 2)
        print(f"Here is your change of: ${change}.")
        global profit
        profit += drink_cost
        return True
        pass
    else:
        print("Sorry, not enough money.")
        return False
# To Do: 5. Make coffee and decrement ingredients from machine
def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")
# while loop flag to keep machine on
machine_on = True
while machine_on:
    user_order = input("What would you like? (espresso/latte/cappuccino)\n").lower()
    if user_order == 'off':
        machine_on = False
    elif user_order == 'report':
        report()
    else:
        drink = MENU[user_order]
        if is_sufficient_resources(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(drink["cost"], payment):
                make_coffee(user_order, drink["ingredients"])
