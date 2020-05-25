from tkinter import *

def onclick():
        if var.get()=="On Click":
            var.set("No Click ")
        else:
            var.set("On Click")

window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('350x200')

var = StringVar()
var.set("On Click")

lbl = Label(window,textvariable=var)
lbl.place(x=0,y=0)

btn = Button(window, text="Click Me", command=onclick)
btn.place(x=20,y=50)

window.mainloop()
