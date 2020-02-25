Num = int(input("Please enter the number : "))
text = "*"
for i in range(Num):
    print((" " * (Num-i)) + text)
    text = text + "**"