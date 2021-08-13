# importing tkinter
from tkinter import *
import math

# creating GUI platform
cal = Tk()
cal.title("Calculator")
cal.iconbitmap("cal.ico")
cal.resizable(width=False, height=False)
cal.maxsize(width=400, height=500)
cal.minsize(width=400, height=500)
calc = Frame(cal, bd=20, pady=5, bg='gainsboro', relief=RIDGE)
calc.grid()


class Calc():

    # creating functions
    def __init__(self):
        self.total = 0
        self.current = ""
        self.input_value = True
        self.check_sum = False
        self.op = ""
        self.result = False

    def numberEnter(self, num):
        self.result = False
        firstnum = screen.get()
        secondnum = str(num)
        if self.input_value:
            self.current = secondnum
            self.input_value = False
        else:
            if secondnum == '.':
                if secondnum in firstnum:
                    return
            self.current = firstnum + secondnum
        self.display(self.current)

    def sum_of_total(self):
        self.result = True
        self.current = float(self.current)
        if self.check_sum == True:
            self.valid_function()
        else:
            self.total = float(screen.get())

    def display(self, value):
        screen.delete(0, END)
        screen.insert(0, value)

    def operation(self, op):
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total = self.current
            self.input_value = True
        self.check_sum = True
        self.op = op
        self.result = False

    def valid_function(self):
        if self.op == "add":
            self.total += self.current
        if self.op == "sub":
            self.total -= self.current
        if self.op == "multi":
            self.total *= self.current
        if self.op == "divide":
            self.total /= self.current

        self.input_value = True
        self.check_sum = False
        self.display(self.total)

    def Clear_Entry(self):
        self.result = False
        self.current = "0"
        self.display(0)
        self.input_value = True

    def all_Clear_Entry(self):
        self.Clear_Entry()
        self.total = 0

    def deleteBs(self):
        numlen = len(screen.get())
        screen.delete(numlen - 1, 'end')
        if numlen == 1:
            screen.insert(0, "0")

    def mathPm(self):
        self.result = False
        self.current = -(float(screen.get()))
        self.display(self.current)


added_value = Calc()
screen = Entry(calc, font=('cambria', 16, 'bold'), bd=20, width=28, justify=RIGHT)
screen.grid(row=0, column=0, columnspan=4, pady=1)
screen.insert(0, "0")

numberpad = "789456123"
i = 0
btn = []

for j in range(3, 6):
    for k in range(3):
        btn.append(Button(calc, width=6, height=2, font=('cambria', 16, 'bold'), bd=4,
                          text=numberpad[i]))
        btn[i].grid(row=j, column=k, pady=1)
        btn[i]["command"] = lambda x=numberpad[i]: added_value.numberEnter(x)
        i += 1

# inserting buttons
btnDelete = Button(calc, width=6, height=2, text="DEL", font=('cambria', 16, 'bold'), bd=4, bg='cadet blue',
                   command=added_value.deleteBs).grid(row=1, column=0, pady=1)
btnClear = Button(calc, width=6, height=2, text=chr(67), font=('cambria', 16, 'bold'), bd=4, bg='cadet blue',
                  command=added_value.Clear_Entry).grid(row=1, column=1, pady=1)
btnClearAll = Button(calc, width=6, height=2, text=chr(67) + chr(69), font=('cambria', 16, 'bold'), bd=4,
                     bg='cadet blue',
                     command=added_value.all_Clear_Entry).grid(row=1, column=2, pady=1)
btnPM = Button(calc, width=6, height=2, text=chr(177), font=('cambria', 16, 'bold'), bd=4, bg='cadet blue',
               command=added_value.mathPm).grid(row=1, column=3, pady=1)
#
btnAdd = Button(calc, width=6, height=2, text="+", font=('cambria', 16, 'bold'), bd=4, bg='cadet blue',
                command=lambda: added_value.operation("add")).grid(row=3, column=3, pady=1)
btnSub = Button(calc, width=6, height=2, text="-", font=('cambria', 16, 'bold'), bd=4, bg='cadet blue',
                command=lambda: added_value.operation("sub")).grid(row=4, column=3, pady=1)
btnMult = Button(calc, width=6, height=2, text="*", font=('cambria', 16, 'bold'), bd=4, bg='cadet blue',
                 command=lambda: added_value.operation("multi")).grid(row=5, column=3, pady=1)
btnDiv = Button(calc, width=6, height=2, text=chr(247), font=('cambria', 16, 'bold'), bd=4, bg='cadet blue',
                command=lambda: added_value.operation("divide")).grid(row=6, column=2, pady=1)
#
btnEqual = Button(calc, width=6, height=2, text='=', font=('cambria', 16, 'bold'), bd=4, bg='cadet blue'
                  , command=added_value.sum_of_total).grid(row=6, column=3, pady=1)
btnZero = Button(calc, width=6, height=2, text="0", font=('cambria', 16, 'bold'), bd=4, bg='cadet blue',
                 command=added_value.numberEnter).grid(row=6, column=1, pady=1)
btnDot = Button(calc, width=6, height=2, text='.', font=('cambria', 16, 'bold'), bd=4, bg='cadet blue',
                command=added_value.numberEnter).grid(row=6, column=0, pady=1)

cal.mainloop()
