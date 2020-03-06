menuList = []
priceList = []

def showBill():
    total = 0
    print("------ My Food ------")
    for i in range(len(menuList)):
        total = total + priceList[i]
        print(f'{menuList[i]:15}{priceList[i]:>10}{total:5} Bath.')

while True:
    menuName = input("Please Enter Menu : ")
    if menuName.capitalize() == "Exit":
        showBill()
        break
    else:
        menuPrice = int(input("Price : "))
        menuList.append(menuName)
        priceList.append(menuPrice)


