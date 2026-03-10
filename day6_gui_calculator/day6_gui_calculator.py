import tkinter as tk

# Create window
window = tk.Tk()
window.title("Day 6 GUI Calculator")
window.geometry("300x400")

# Create calculator display
entry = tk.Entry(window, width=16, font=('Arial', 24), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

#Function
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

#Button
button1 = tk.Button(window, text="1", padx=20, pady=20, command=lambda: button_click(1))
button2 = tk.Button(window, text="2", padx=20, pady=20, command=lambda: button_click(2))
button3 = tk.Button(window, text="3", padx=20, pady=20, command=lambda: button_click(3))

button4 = tk.Button(window, text="4", padx=20, pady=20, command=lambda: button_click(4))
button5 = tk.Button(window, text="5", padx=20, pady=20, command=lambda: button_click(5))
button6 = tk.Button(window, text="6", padx=20, pady=20, command=lambda: button_click(6))

button7 = tk.Button(window, text="7", padx=20, pady=20, command=lambda: button_click(7))
button8 = tk.Button(window, text="8", padx=20, pady=20, command=lambda: button_click(8))
button9 = tk.Button(window, text="9", padx=20, pady=20, command=lambda: button_click(9))

button0 = tk.Button(window, text="0", padx=20, pady=20, command=lambda: button_click(0))

#other button
button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button0.grid(row=4, column=1)


#operatiom
f_num = 0
math = ""

def button_clear():
    entry.delete(0, tk.END)


def button_add():
    global f_num
    global math
    math = "addition"
    f_num = int(entry.get())
    entry.delete(0, tk.END)


def button_subtract():
    global f_num
    global math
    math = "subtraction"
    f_num = int(entry.get())
    entry.delete(0, tk.END)


def button_multiply():
    global f_num
    global math
    math = "multiplication"
    f_num = int(entry.get())
    entry.delete(0, tk.END)


def button_divide():
    global f_num
    global math
    math = "division"
    f_num = int(entry.get())
    entry.delete(0, tk.END)

#other button 2 as in (calculation sign)
button_add = tk.Button(window, text="+", padx=20, pady=20, command=button_add)
button_subtract = tk.Button(window, text="-", padx=20, pady=20, command=button_subtract)
button_multiply = tk.Button(window, text="*", padx=20, pady=20, command=button_multiply)
button_divide = tk.Button(window, text="/", padx=20, pady=20, command=button_divide)

button_clear = tk.Button(window, text="C", padx=20, pady=20, command=button_clear)

button_clear.grid(row=4, column=0)

button_add.grid(row=1, column=3)
button_subtract.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4, column=3)

#Button + sign
def button_equal():
    second_number = int(entry.get())
    entry.delete(0, tk.END)
    
    if math == "addition":
        entry.insert(0, f_num + second_number)
    elif math == "subtraction":
        entry.insert(0, f_num - second_number)
    elif math == "multiplication":
        entry.insert(0, f_num * second_number)
    elif math == "division":
        if second_number == 0:
            entry.insert(0, "Error")
        else:
            entry.insert(0, f_num / second_number)

equal_button = tk.Button(window, text="=", padx=20, pady=20, command=button_equal)
equal_button.grid(row=4, column=2)  # place it in the grid

window.mainloop()