from tkinter import *

# Setting Root
root = Tk()
root.title("Calculus")
root.config(bg="white")
root.resizable(False, False)

# Design Variables
btnpadx = 5
btnpady = 5
screenNum = StringVar()
screenNum.set("")


# Global Calculus Variables
operacion = ""
result = 0


# Setting Main Frame
main_frame = Frame()
main_frame.pack(fill="both", expand="True")
main_frame.config(bg="white")
main_frame.config(padx=5, pady=5)

# -------- Widget View Operations Screen -----------------------
screenView = Label(main_frame)

screenView.grid(row=1, column=1, columnspan=4, sticky="nsew")
screenView.config(bg="grey", fg="yellow")
screenView.config(text="0")

# -------- Widget Calculus Screen -----------------------
screen = Entry(main_frame, textvariable=screenNum)
screen.grid(row=2, column=1, columnspan=4, sticky="nsew")
screen.config(bg="black", fg="#03f943")


# -------- Actions Btns --------------------------------
def btn_action(num):
    global operacion

    if operacion != "":
        screenNum.set(num)
        operacion = ""
    else:
        screenNum.set(screenNum.get() + num)


# -------- Function Sum --------------------------------
def suma(num):
    global result
    global operacion
    operacion = "suma"
    result += float(num)
    screenNum.set(result)


# -------- Clear Screen --------------------------------
def btn_clear():
    global cal_operation
    global result
    global straux
    result = 0
    screenNum.set("0")
    screenView.configure(text='')


# ------------ Excetute the calculus Operation -----------
def btn_eq():
    global result
    global operacion

    print("Resultado: ", result)
    print("operacion: ", operacion)
    if operacion == 'suma':
        result += float(screenNum.get())
    elif operacion == '-':
        result = float(result) - float(screenNum.get())
    elif operacion == '*':
        result = float(result) * float(screenNum.get())
    elif operacion == '/':
        result = float(result) / float(screenNum.get())
    screenNum.set(str(result))
    result = 0


# -------- Row 1 ---------------------------------------
btn7 = Button(main_frame, text="7", width=3, padx=btnpadx, pady=btnpady, command=lambda: btn_action("7"))
btn7.grid(row=3, column=1)
btn8 = Button(main_frame, text="8", width=3, padx=btnpadx, pady=btnpady, command=lambda: btn_action("8"))
btn8.grid(row=3, column=2)
btn9 = Button(main_frame, text="9", width=3, padx=btnpadx, pady=btnpady, command=lambda: btn_action("9"))
btn9.grid(row=3, column=3)
btnDiv = Button(main_frame, text="/", width=3, padx=btnpadx, pady=btnpady, command=lambda: operand("/"))
btnDiv.grid(row=3, column=4)

# -------- Row 2 ---------------------------------------
btn4 = Button(main_frame, text="4", width=3, padx=btnpadx, pady=btnpady, command=lambda: btn_action("4"))
btn4.grid(row=4, column=1)
btn5 = Button(main_frame, text="5", width=3, padx=btnpadx, pady=btnpady, command=lambda: btn_action("5"))
btn5.grid(row=4, column=2)
btn6 = Button(main_frame, text="6", width=3, padx=btnpadx, pady=btnpady, command=lambda: btn_action("6"))
btn6.grid(row=4, column=3)
btnMul = Button(main_frame, text="X", width=3, padx=btnpadx, pady=btnpady, command=lambda: operand("*"))
btnMul.grid(row=4, column=4)

# -------- Row 3 ---------------------------------------
btn1 = Button(main_frame, text="1", width=3, padx=btnpadx, pady=btnpady, command=lambda: btn_action("1"))
btn1.grid(row=5, column=1)
btn2 = Button(main_frame, text="2", width=3, padx=btnpadx, pady=btnpady, command=lambda: btn_action("2"))
btn2.grid(row=5, column=2)
btn3 = Button(main_frame, text="3", width=3, padx=btnpadx, pady=btnpady, command=lambda: btn_action("3"))
btn3.grid(row=5, column=3)
btnSubs = Button(main_frame, text="-", width=3, padx=btnpadx, pady=btnpady, command=lambda: operand("-"))
btnSubs.grid(row=5, column=4)

# -------- Row 4 ---------------------------------------
btn0 = Button(main_frame, text="0", width=3, padx=btnpadx, pady=btnpady, command=lambda: btn_action("0"))
btn0.grid(row=6, column=1)
btnCom = Button(main_frame, text=",", width=3, padx=btnpadx, pady=btnpady, command=lambda: btn_action(","))
btnCom.grid(row=6, column=2)
btnClear = Button(main_frame, text="C", width=3, padx=btnpadx, pady=btnpady, command=lambda: btn_clear())
btnClear.grid(row=6, column=3)
btnSum = Button(main_frame, text="+", width=3, padx=btnpadx, pady=btnpady, command=lambda: suma(screenNum.get()))
btnSum.grid(row=6, column=4)

# -------- Row 5 ---------------------------------------
btnEq = Button(main_frame, text="=", width=3, padx=btnpadx, pady=btnpady, command=lambda: btn_eq())
btnEq.grid(row=7, column=1, columnspan=4, sticky="nsew")

root.mainloop()
