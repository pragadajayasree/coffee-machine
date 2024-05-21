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
    print("please insert coins")
    x = int(input("How many quarters? "))
    y = int(input("How many dines? "))
    z = int(input("How many nickles? "))
    s = int(input("How many pennies? "))
    amount = x * 0.25 + y * 0.10 + z * 0.05 + s * 0.01
    return amount


def check(amount, m):
    if amount < m["cost"]:
        return 0
    else:
        return 1


def change(s, amount, m):
    if amount != s["cost"]:
        print(f"Here is ${round(amount - s["cost"], 2)} in change")
    print(f"here is your {m} ☕ enjoy!")


def deduct(s):
    global money
    for i in s["ingredients"]:
        resources[i] -= s["ingredients"][i]
    money += s["cost"]


def satisfy(s):
    for i in s:
        if resources[i] < s[i]:
            print(f"sorry! there is no enough {i}")
            return 0
    return 1


def select(s, m):
    q = satisfy(s["ingredients"])
    if q:
        amount = coins()
        if check(amount, s) == 0:
            print("sorry!,that's not enough money. money refunded.")
        else:
            change(s, amount, m)
            deduct(s)


a = True
while a:
    p = input(" What would you like ? report or (espresso , latte , cappuccino) :")
    if p == "report":
        report()
    else:
        select(MENU[p], p)
