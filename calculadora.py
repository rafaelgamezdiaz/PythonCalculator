from tkinter import *

# Setting Root
root = Tk()
root.title("Calculus")
root.config(bg="white")
# root.geometry("250x300")
root.resizable(False, False)

# Design Variables
btnpadx = 5
btnpady = 5
screenNum = StringVar()
operand1 = StringVar()


# Setting Main Frame
main_frame = Frame()
main_frame.pack(fill="both", expand="True")
main_frame.config(bg="white")
main_frame.config(padx=5, pady=5)

# -------- Widget Results Screen -----------------------
screen = Entry(main_frame, textvariable=screenNum)
screenNum.set("0")
screen.grid(row=1, column=1, columnspan=4, sticky="nsew")
screen.config(bg="black", fg="#03f943")


# -------- Actions Btns --------------------------------
def btn_action(num):
    if num == "0" and screenNum.get() == "0":
        screenNum.set(num)
    elif num != "0" and screenNum.get() == "0":
        screenNum.set(num)
    else:
        screenNum.set(screenNum.get() + num)


# -------- Class Operations --------------------------------
class Operations:

    value1 = 0
    operation = "+"

    def set_operation(self, operation):
        self.operation = operation
        self.value1 = screenNum.get()
        print(f"Setting the operation {screenNum.get()}")


def operand1(instance, theop):
    instance.set_operation(theop)
    screenNum.set('0')


def btn_make(instance):

    if instance.operation == '+':
        screenNum.set(str(float(instance.value1) + float(screenNum.get())))
    elif instance.operation == '-':
        screenNum.set(float(instance.value1) - float(screenNum.get()))
    elif instance.operation == '*':
        screenNum.set(float(instance.value1) * float(screenNum.get()))
    elif instance.operation == '/':
        screenNum.set(float(instance.value1) / float(screenNum.get()))


# -------- Instantiate the Operation ---------------------------------------
op = Operations()


# -------- Row 1 ---------------------------------------
btn7 = Button(main_frame, text="7", width=3, padx=btnpadx, pady=btnpady, command=lambda: btn_action("7"))
btn7.grid(row=2, column=1)
btn8 = Button(main_frame, text="8", width=3, padx=btnpadx, pady=btnpady, command=lambda: btn_action("8"))
btn8.grid(row=2, column=2)
btn9 = Button(main_frame, text="9", width=3, padx=btnpadx, pady=btnpady, command=lambda: btn_action("9"))
btn9.grid(row=2, column=3)
btnDiv = Button(main_frame, text="/", width=3, padx=btnpadx, pady=btnpady, command=lambda: operand1(op, "/"))
btnDiv.grid(row=2, column=4)

# -------- Row 2 ---------------------------------------
btn4 = Button(main_frame, text="4", width=3, padx=btnpadx, pady=btnpady, command=lambda: btn_action("4"))
btn4.grid(row=3, column=1)
btn5 = Button(main_frame, text="5", width=3, padx=btnpadx, pady=btnpady, command=lambda: btn_action("5"))
btn5.grid(row=3, column=2)
btn6 = Button(main_frame, text="6", width=3, padx=btnpadx, pady=btnpady, command=lambda: btn_action("6"))
btn6.grid(row=3, column=3)
btnMul = Button(main_frame, text="X", width=3, padx=btnpadx, pady=btnpady, command=lambda: operand1(op, "*"))
btnMul.grid(row=3, column=4)

# -------- Row 3 ---------------------------------------
btn1 = Button(main_frame, text="1", width=3, padx=btnpadx, pady=btnpady, command=lambda: btn_action("1"))
btn1.grid(row=4, column=1)
btn2 = Button(main_frame, text="2", width=3, padx=btnpadx, pady=btnpady, command=lambda: btn_action("2"))
btn2.grid(row=4, column=2)
btn3 = Button(main_frame, text="3", width=3, padx=btnpadx, pady=btnpady, command=lambda: btn_action("3"))
btn3.grid(row=4, column=3)
btnSubs = Button(main_frame, text="-", width=3, padx=btnpadx, pady=btnpady, command=lambda: operand1(op, "-"))
btnSubs.grid(row=4, column=4)

# -------- Row 4 ---------------------------------------
btn0 = Button(main_frame, text="0", width=3, padx=btnpadx, pady=btnpady, command=lambda: btn_action("0"))
btn0.grid(row=5, column=1)
btnCom = Button(main_frame, text=",", width=3, padx=btnpadx, pady=btnpady, command=lambda: btn_action(","))
btnCom.grid(row=5, column=2)
btnEq = Button(main_frame, text="=", width=3, padx=btnpadx, pady=btnpady, command=lambda: btn_make(op))
btnEq.grid(row=5, column=3)
btnSum = Button(main_frame, text="+", width=3, padx=btnpadx, pady=btnpady, command=lambda: operand1(op, "+"))
btnSum.grid(row=5, column=4)

root.mainloop()
