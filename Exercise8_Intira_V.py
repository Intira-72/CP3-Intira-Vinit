userName = input("Username : ")
passWord = input("Password : ")

if userName == "customer01" and passWord == "customer2019":
    print("---- M Shop ยินดีต้อนรับ ----")
    print("1. Chocolate - 10 Bath")
    print("2. Milk      - 15 Bath")
    print("3. Candy     - 5  Bath")
    print("4. Pen       - 16 Bath")
    print("5. Water     - 13 Bath")
    userSelected = int(input("กรุณาเลือกรายการสินค้า : "))
    if userSelected == 1:
        total = int(input("กรอกจำนวนที่ต้องการ : "))
        print("-------------------------------")
        print("Chocolate จำนวน", total, "ชิ้น")
        print("จำนวนเงินที่ต้องชำระ = ", total*10, "บาท")
        print("-------------------------------")
    elif userSelected == 2:
        total = int(input("กรอกจำนวนที่ต้องการ : "))
        print("-------------------------------")
        print("Milk จำนวน", total, "กล่อง")
        print("จำนวนเงินที่ต้องชำระ = ", total*15, "บาท")
        print("-------------------------------")
    elif userSelected == 3:
        total = int(input("กรอกจำนวนที่ต้องการ : "))
        print("-------------------------------")
        print("Candy จำนวน", total, "ชิ้น")
        print("จำนวนเงินที่ต้องชำระ = ", total*5, "บาท")
        print("-------------------------------")
    elif userSelected == 4:
        total = int(input("กรอกจำนวนที่ต้องการ : "))
        print("-------------------------------")
        print("Pen จำนวน", total, "กล่อง")
        print("จำนวนเงินที่ต้องชำระ = ", total*16, "บาท")
        print("-------------------------------")
    elif userSelected == 5:
        total = int(input("กรอกจำนวนที่ต้องการ : "))
        print("-------------------------------")
        print("Water จำนวน", total, "ขวด")
        print("จำนวนเงินที่ต้องชำระ = ", total*13, "บาท")
        print("-------------------------------")
    print("ขอบคุณค่ะ")
else:
    print("Username หรือ Password ไม่ถูกต้อง")