from tkinter import *

window = Tk()
window.geometry("328x370+530+130")
window.title("Calculator by Tahir Habib")
window.configure(bg='black')

# Arithmetic Functions & codes for button widgets to work


def press(number):
    textfield.insert(END, number)


def button_divide():
    num = textfield.get()
    global firstNumber
    global operator
    operator = "divide"
    firstNumber = float(num)
    textfield.delete(0, END)


def button_multiply():
    num = textfield.get()
    global firstNumber
    global operator
    operator = "multiply"
    firstNumber = float(num)
    textfield.delete(0, END)


def button_subtract():
    num = textfield.get()
    global firstNumber
    global operator
    operator = "subtract"
    firstNumber = float(num)
    textfield.delete(0, END)


def button_add():
    num = textfield.get()
    global firstNumber
    global operator
    operator = "add"
    firstNumber = float(num)
    textfield.delete(0, END)


def button_equals():
    second_num = textfield.get()
    textfield.delete(0, END)

    if operator == "add":
        textfield.insert(0, float(second_num) + float(firstNumber))
    if operator == "multiply":
        textfield.insert(0, float(second_num) * float(firstNumber))
    if operator == "divide":
        textfield.insert(0, float(firstNumber) / float(second_num))
    if operator == "subtract":
        textfield.insert(0, float(firstNumber) - float(second_num))


def button_clear():
    textfield.delete(0, END)


# Button Widgets for "C" or clear button
textfield = Entry(window, bd=15, bg="black",fg="white", font=("bold", '25'), justify="right", width=294)
textfield.pack(fill='x')

buttonC = Button(window, text='C', fg='black',bg="grey64", height=2, width=294, font='bold', command=button_clear)
buttonC.pack(fill='x')

# Button Widgets from button 7 to minus sign button (using grid parameter)
button_frame = Frame()
button_frame.pack(side='top', fill='x')

button7 = Button(button_frame, text='7', fg='white',bg="grey18", height=2, width=8, font=('bold'), command=lambda: press(7))
button8 = Button(button_frame, text='8', fg='white',bg="grey18", height=2, width=8, font=('bold'), command=lambda: press(8))
button9 = Button(button_frame, text='9', fg='white',bg="grey18", height=2, width=8, font=('bold'), command=lambda: press(9))
buttonDiv = Button(button_frame, text='/', fg='white',bg="darkgoldenrod1", height=2, width=8, font=('bold'), command=button_divide)
button4 = Button(button_frame, text='4', fg='white',bg="grey18", height=2, width=8, font=('bold'), command=lambda: press(4))
button5 = Button(button_frame, text='5', fg='white',bg="grey18", height=2, width=8, font=('bold'), command=lambda: press(5))
button6 = Button(button_frame, text='6', fg='white',bg="grey18", height=2, width=8, font=('bold'), command=lambda: press(6))
buttonMul = Button(button_frame, text='*', fg='white',bg="darkgoldenrod1", height=2, width=8, font=('bold'), command=button_multiply)
button1 = Button(button_frame, text='1', fg='white',bg="grey18", height=2, width=8, font=('bold'), command=lambda: press(1))
button2 = Button(button_frame, text='2', fg='white',bg="grey18", height=2, width=8, font=('bold'), command=lambda: press(2))
button3 = Button(button_frame, text='3', fg='white',bg="grey18", height=2, width=8, font=('bold'), command=lambda: press(3))
buttonSub = Button(button_frame, text='-', fg='white',bg="darkgoldenrod1", height=2, width=8, font=('bold'), command=button_subtract)

button_frame.columnconfigure(4, weight=1)
button_frame.configure(bg='black')
button7.grid(row=3, column=0)
button8.grid(row=3, column=1)
button9.grid(row=3, column=2)
buttonDiv.grid(row=3, column=3)
button4.grid(row=4, column=0)
button5.grid(row=4, column=1)
button6.grid(row=4, column=2)
buttonMul.grid(row=4, column=3)
button1.grid(row=5, column=0)
button2.grid(row=5, column=1)
button3.grid(row=5, column=2)
buttonSub.grid(row=5, column=3)

# Button Widgets from button 0 to plus sign button (using grid parameter)
button_frame1 = Frame()
button_frame1.pack(fill='x')

button0 = Button(button_frame1, text='0', fg='white',bg="grey18", height=2, width=11, font='bold', command=lambda: press('0'))
buttonDot = Button(button_frame1, text='.', fg='white',bg="grey18", height=2, width=11, font='bold', command=lambda: press('.'))
buttonAdd = Button(button_frame1, text='+', fg='white',bg="darkgoldenrod1", height=2, width=11, font='bold', command=button_add)

button_frame1.columnconfigure(1, weight=1)
button_frame1.configure(bg='black')
button0.grid(row=6, column=0)
buttonDot.grid(row=6, column=1)
buttonAdd.grid(row=6, column=2)

# Button Widgets for equal sign button
buttonEq = Button(window, text='=', fg='white',bg="darkgoldenrod1", height=2, width=294, font='bold', command=button_equals)
buttonEq.pack(side='bottom', fill='x')

window.mainloop()