from tkinter import *
import math

window = Tk()
window.title("Miles to Kilometers")
window.config(padx=50, pady=50)

value = Entry(width=5)
value.focus()
value.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=0, row=1)

is_amount = Label(text="0")
is_amount.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)


def but_click():
    new_text = value.get()
    calc = str(round(int(new_text) * 1.609, 2))
    is_amount.config(text=calc)


button = Button(text="Calculate", command=but_click)
button.grid(column=1, row=2)

window.mainloop()
