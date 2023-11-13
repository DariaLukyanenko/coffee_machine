from data import MENU
from data import resources

MACHINE_MONEY = 0
MEASURUMENT_UNITS = ['ml','ml','g']

def report(coffee):
    for ingridient, unit in zip(resources, MEASURUMENT_UNITS):
            print(f'{ingridient.capitalize()}: {resources[ingridient]}{unit}')
    print(f'Money: {MACHINE_MONEY}$')

def check_resources(coffee):
    not_enough_products = 0
    for ingredient, amount in MENU[coffee]['ingredients'].items(): 
         if amount>resources[ingredient]:
             print(f"Sorry, there are not enough {ingredient}")
             not_enough_products += 1
             
    if not_enough_products > 0:
        return False
        
    return True

def process_coins(suma=0):
    quarters = int(input('How many quarters?'))
    dimes = int(input('How many dimes?'))
    nickles = int(input('How many nickles?'))
    pennies = int(input('How many pennies?'))
    suma = 0.25*quarters+0.1*dimes+0.05*nickles+0.01*pennies 
    return suma

def process_resources(coffee):
    for ingridient, znachenie in MENU[coffee]['ingredients'].items():
        resources[ingridient] -= MENU[coffee]['ingredients'][ingridient]

def process_money(coffee):
    global MACHINE_MONEY
    MACHINE_MONEY+=MENU[coffee]['cost']
    return MACHINE_MONEY

def process_transaction(suma,coffee):
    if suma<MENU[coffee]['cost']:
        print("Not enough money")
        return False
    if suma>=MENU[coffee]['cost']:
        print(f"Here is {round(suma-MENU[coffee]['cost'],2)} in change")
        return True
        
def coffee_machine():
    coffee = input("what would you like? (espresso/latte/capuccino): ")
    if coffee == "report":
        report(coffee)
    
    if coffee in MENU:
        if check_resources(coffee):
            suma = process_coins()
            if process_transaction(suma,coffee):
                process_resources(coffee)
                process_money(coffee)
                print(f"Enjoy your {coffee}")
                return


process=False
while process !=True :
    coffee_machine()
    
