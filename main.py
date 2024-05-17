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
money = 0
def report():
    print("water:", resources["water"], "ml")
    print("milk:", resources["milk"], "ml")
    print("coffee:", resources["coffee"], "g")
    print("money: $", money)
def coins():
     print ("please insert coins")
     x = int(input("How many quarters? "))
     y = int(input("How many dines? "))
     z = int(input("How many nickles? "))
     s = int(input("How many pennies? "))
     amount = x*0.25+y*0.10+z*0.05+s*0.01
     return amount

def check(amount,p):
    if amount < p["cost"]:
        return 0
    else:
        return 1
def change(p,amount,m):
    if amount !=p["cost"]:
        print(f"Here is ${round(amount-p["cost"],2)} in change")
    print(f"here is your {m} ☕ enjoy!")

def deduct(p):
    global money
    for i in p["ingredients"]:
        resources[i]-=p["ingredients"][i]
    money+=p["cost"]

def satisfy(p):
    for i in p:
        if resources[i]<p[i]:
            print(f"sorry! there is no enough {i}")
            return 0
    return 1

def select(p,m):
    q=satisfy(p["ingredients"])
    if(q):
        amount = coins()
        if check(amount,p) == 0:
            print("sorry!,that's not enough money. money refunded.")
        else:
            change(p,amount,m)
            deduct(p)



a = True
while a:
    p = input(" What would you like ? report or (espresso , latte , cappuccino) :")
    if p == "report":
        report()
    else:
       select(MENU[p],p)
