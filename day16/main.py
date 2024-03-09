from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee = CoffeeMaker()
money = MoneyMachine()

live = True

while live:
    choice = input(f"what do you want to order? {menu.get_items()} : ")
    if choice == "report":
        coffee.report()
        money.report()
    if choice == "off":
        live = False
    else:
        drink = menu.find_drink(choice)
        if coffee.is_resource_sufficient(drink) and money.make_payment(drink.cost):
            coffee.make_coffee(drink)

