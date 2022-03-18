from tkinter import *
from time import *

def update():
    timeString = strftime("%I:%M:%S %p")
    timeLabel.config(text=timeString)
    dayString = strftime("%A")
    dayLabel.config(text=dayString)
    dateString = strftime("%B %d, %Y")
    dateLabel.config(text=dateString)
    window.after(1000,update)

window = Tk()

timeLabel = Label(window,font=("futura",50),fg="green",bg="black")
timeLabel.pack()

dayLabel = Label(window,font=("futura",25))
dayLabel.pack()

dateLabel = Label(window,font=("futura",15))
dateLabel.pack()

update()

window.mainloop()
