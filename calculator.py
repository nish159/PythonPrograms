from tkinter import *

def buttonPress(num):
    
    global equationText
    equationText = equationText + str(num)
    equationLabel.set(equationText)

def equals():
    
    global equationText
    try:
        
        total = str(eval(equationText))
        equationLabel.set(total)
        equationText = total
    
    except SyntaxError:
        equationLabel.set("syntax error")
        equationText = ""
    except ZeroDivisionError:
        equationLabel.set("arithmetic error")
        equationText = ""

def clear():
    
    global equationText
    equationLabel.set("")
    equationText = ""

window = Tk()
window.title("calculator program")
window.geometry("575x575")
window.config(bg="#636363")

equationText = ""

equationLabel = StringVar()

label = Label(window, textvariable=equationLabel, font=('consolas',20), bg="white", width=24, height=2)
label.pack()

frame = Frame(window)
frame.pack()

button1 = Button(frame, text=1, height=4, width=9, font=35, command=lambda: buttonPress(1), activebackground="#7193a6")
button1.grid(row=0, column=0)

button2 = Button(frame, text=2, height=4, width=9, font=35, command=lambda: buttonPress(2), activebackground="#7193a6")
button2.grid(row=0, column=1)

button3 = Button(frame, text=3, height=4, width=9, font=35, command=lambda: buttonPress(3), activebackground="#7193a6")
button3.grid(row=0, column=2)

button4 = Button(frame, text=4, height=4, width=9, font=35, command=lambda: buttonPress(4), activebackground="#7193a6")
button4.grid(row=1, column=0)

button5 = Button(frame, text=5, height=4, width=9, font=35, command=lambda: buttonPress(5), activebackground="#7193a6")
button5.grid(row=1, column=1)

button6 = Button(frame, text=6, height=4, width=9, font=35, command=lambda: buttonPress(6), activebackground="#7193a6")
button6.grid(row=1, column=2)

button7 = Button(frame, text=7, height=4, width=9, font=35, command=lambda: buttonPress(7), activebackground="#7193a6")
button7.grid(row=2, column=0)

button8 = Button(frame, text=8, height=4, width=9, font=35, command=lambda: buttonPress(8), activebackground="#7193a6")
button8.grid(row=2, column=1)

button9 = Button(frame, text=9, height=4, width=9, font=35, command=lambda: buttonPress(9), activebackground="#7193a6")
button9.grid(row=2, column=2)

button0 = Button(frame, text=0, height=4, width=9, font=35, command=lambda: buttonPress(0), activebackground="#7193a6")
button0.grid(row=3, column=0)

plus = Button(frame, text='+', height=4, width=9, font=35, command=lambda: buttonPress('+'), activebackground="#7193a6")
plus.grid(row=0, column=3)

minus = Button(frame, text='-', height=4, width=9, font=35, command=lambda: buttonPress('-'), activebackground="#7193a6")
minus.grid(row=1, column=3)

multiply = Button(frame, text='*', height=4, width=9, font=35, command=lambda: buttonPress('*'), activebackground="#7193a6")
multiply.grid(row=2, column=3)

divide = Button(frame, text='+', height=4, width=9, font=35, command=lambda: buttonPress('/'), activebackground="#7193a6")
divide.grid(row=3, column=3)

equal = Button(frame, text='=', height=4, width=9, font=35, command=equals, activebackground="#7193a6")
equal.grid(row=3, column=2)

decimal = Button(frame, text='.', height=4, width=9, font=35, command=lambda: buttonPress('.'), activebackground="#7193a6")
decimal.grid(row=3, column=1)

clear = Button(window, text='clear', height=4, width=12, font=35, command=clear, activebackground="#7193a6")
clear.pack()

window.mainloop()
