from tkinter import *

window = Tk()
window.title("event_handler")
window.geometry("400x400")

def keypress(event):
    print(event.char)
window.bind("<Key>", keypress)

def button(event):
    print("click me!")

buton = Button(text = "Click me!")
buton.pack()
buton.bind("<Button-1>", button)

window.mainloop()

