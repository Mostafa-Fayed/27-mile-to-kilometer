from tkinter import *

window = Tk()
window.config(padx=20, pady=20)
window.title("Mile to Km Converter")

user_input = Entry(width=10)
user_input.config(font=("Arial", 12))
user_input.grid(column=1, row=0)


miles_label = Label(text="Miles", font=("Arial", 12))
miles_label.config(padx=10, pady=5)
miles_label.grid(column=2, row=0)

converter_text = Label(text="is equal to", font=("Arial", 12))
converter_text.config(padx=10, pady=5)
converter_text.grid(column=0, row=1)

answer = Label(text="", font=("Arial", 12))
answer.grid(column=1, row=1)

km_text = Label(text="Km", font=("Arial", 12))
km_text.grid(column=2, row=1)


def calculate():
    no_of_miles = float(user_input.get())
    no_of_km = no_of_miles * 1.609
    answer.config(text=f"{no_of_km}")


button = Button(text="Calculate", font=("Arial", 12), command=calculate)
button.grid(column=1, row=2)



window.mainloop()