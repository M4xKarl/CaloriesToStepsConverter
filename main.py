from tkinter import *

# def button_clicked():
#     if(height_var = 0 or hei)


FONT = "Arial", 16, "bold"
BUTTON_FONT = "Arial", 14


def button_clicked():
    weight = float(weight_input.get())
    calories = float(calories_input.get())

    if weight > 0 and calories > 0:
        steps = calories / (weight * 0.7) * 1300
        steps_result_label.config(text=str(int(steps)))

        time = (steps / 1300) / 5 * 60
        time_result_label.config(text=f"{str(int(time))} min")


def button_exit():
    window.destroy()


# Window and title

window = Tk()
window.title("Converter")
window.minsize(width=410, height=320)
window.config(padx=20)
my_title = Label(text="Calories to steps converter", font=FONT)
my_title.grid(column=0, row=0, columnspan=3)
my_title.config(pady=20, padx=30)

# Labels

weight_label = Label(text="Weight (kg):", font=FONT)
weight_label.config(pady=10, padx=10)
weight_label.grid(column=0, row=1, sticky="e")

calories_label = Label(text="Calories to burn:", font=FONT)
calories_label.config(pady=10, padx=10)
calories_label.grid(column=0, row=2, sticky="e")

steps_label = Label(text="Steps:", font=FONT)
steps_label.config(pady=10, padx=10)
steps_label.grid(column=0, row=3, sticky="e")

steps_result_label = Label(text="0", font=FONT)
steps_result_label.config(pady=10)
steps_result_label.grid(column=1, row=3, sticky="w", columnspan=2)

time_result_label = Label(text="0", font=FONT)
time_result_label.config(pady=10)
time_result_label.grid(column=1, row=4, sticky="w", columnspan=2)

time_label = Label(text="Average time:", font=FONT)
time_label.config(pady=10, padx=10)
time_label.grid(column=0, row=4, sticky="e")

# Inputs

weight_input = Entry(width=10)
weight_input.insert(END, "0")
weight_input.grid(column=1, row=1, sticky="w")

calories_input = Entry(width=10)
calories_input.insert(END, "0")
calories_input.grid(column=1, row=2, sticky="w")

# Button

button1 = Button(text="Calculate", font=BUTTON_FONT, command=button_clicked)
button1.grid(column=1, row=5, sticky="w")
button1.config(width=8)

button2 = Button(text="Exit", font=BUTTON_FONT, command=button_exit)
button2.grid(column=0, row=5)
button2.config(width=8)

window.mainloop()
