# Function Example 2
def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        showMenu()
    else:
        login()

def showMenu():
    print("----- M Shop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    print("----- please select -----")

    userSelect = menuSelect()

    if userSelect == 1:
        print(vatCalculate(int(input("Price (THB) : "))))
    elif userSelect == 2:
        print(priceCalculate())

def menuSelect():
    userSelected = int(input(">> "))
    return userSelected

def vatCalculate(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return result

def priceCalculate():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCalculate(price1 + price2)

login()