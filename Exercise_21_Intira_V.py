from tkinter import *
import math

def leftClickButton(event):
    bmiCal = float(textWeight.get()) / math.pow(float(textHeight.get()) / 100, 2)

    if bmiCal > 29.9:
        labelCalculate.configure(text=str(round(bmiCal)) + " => อ้วนมาก")
    elif bmiCal > 24.9:
        labelCalculate.configure(text=str(round(bmiCal)) + " => อ้วน")
    elif bmiCal > 22.9:
        labelCalculate.configure(text=str(round(bmiCal)) + " => น้ำหนักเกิน")
    elif bmiCal > 18.5:
        labelCalculate.configure(text=str(round(bmiCal)) + " => น้ำหนักปกติ")
    else:
        labelCalculate.configure(text=str(round(bmiCal)) + " => ผอมเกินไป")

main = Tk()

labelHeight = Label(main, text="Height (cm.) : ")
labelHeight.grid(row=0, column=0)
textHeight = Entry(main)
textHeight.grid(row=0, column=1)

labelWeight = Label(main, text="Weight (km.) : ")
labelWeight.grid(row=1, column=0)
textWeight = Entry(main)
textWeight.grid(row=1, column=1)

labelCalculate = Label(main)
labelCalculate.grid(row=2, column=1)

btnCalculate = Button(main, text="Calculate")
btnCalculate.bind('<Button-1>', leftClickButton)
btnCalculate.grid(row=2, column=0)

main.mainloop()