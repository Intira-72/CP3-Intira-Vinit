def vatCalculate():
    Num = int(input("Please enter the number : "))
    result = Num + (Num * 7 / 100)
    return result

print(vatCalculate())