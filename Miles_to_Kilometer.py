from tkinter import *

def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    kilometer_result_label.config(text = f"{km}")

window = Tk()
window.title("Miles to kilometer converter")
window.minsize(width=700,height=400,)
window.config(padx=250,pady=150)

miles_input = Entry(width = 20)
miles_input.grid(column=1, row=0)

miles_label = Label(text = "Miles",font=[30])
miles_label.grid(column=2, row=0)

is_equal_label = Label(text = "is equal to",font=[30])
is_equal_label.grid(column=0,row=1)

kilometer_result_label = Label(text="0",font=[30])
kilometer_result_label.grid(column=1, row=1)

kilometer_label = Label(text="km",font=[30])
kilometer_label.grid(column=2, row=1)

calculate_button = Button(text = "Calculate",command=miles_to_km,width=20,height=2,font=[30])
calculate_button.grid(column=1, row=2)

window.mainloop()
