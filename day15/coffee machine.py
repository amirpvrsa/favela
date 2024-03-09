#coffee machine
from MENU import menu
from MENU import resource

off = False

def req_coffee():
    a=input("what would you like ? (esspresso(1.5$)/latte](2.5$)/cappuchino(3$)) : ")
    return a


def req_money():
    print("please insert coin!")
    a=int(input("how many quartes ? : "))
    b=int(input("how many dimes ? : "))
    c=int(input("how many nickles ? : "))
    d=int(input("how many pennies ? : "))
    total_money = (a/4)+(b/10)+(c/20)+(d/100)
    resource["money"]+= total_money
    return total_money




def money_comparion(coffee, money):
    print(menu[coffee]["cost"])
    print(money)
    if menu[coffee]["cost"] > money:
        print("money is not enough!")
        return False
    
live=True
def resource_changer_checker(coffee,money):
    if resource["water"] < menu[coffee]["ingredients"]["water"]:
        print("sorry there is not enough water!")
    if resource["milk"] < menu[coffee]["ingredients"]["milk"]:
        print("sorry there is not enough milk!")
    if resource["coffee"] < menu[coffee]["ingredients"]["coffee"]:
        print("sorry there is not enough water!")
    if resource["money"] < menu[coffee]["cost"]:
        print("sorry thats not enough money, money refunded")
        resource["money"] -= money
    else:
        resource["water"] -= menu[coffee]["ingredients"]["water"]
        resource["milk"] -= menu[coffee]["ingredients"]["milk"]
        resource["coffee"] -= menu[coffee]["ingredients"]["coffee"]
        resource["money"] = money - menu[coffee]["cost"]
        print(f"here is ${resource["money"]} change.")
        print(f"here is your {coffee}, enjoy it!")

def coffee():
    live=True
    while live:
        a=req_coffee()
        if a=="off":
            live=False
        if live:
            b=req_money()
            resource_changer_checker(a,b)
        

coffee()
    
    