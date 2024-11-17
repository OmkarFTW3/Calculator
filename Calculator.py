import tkinter as tk




# Function to open a calculator window
def open_calculator():
    calc_window = tk.Toplevel(root)
    calc_window.title("Calculator")

    # Function to update the expression in the entry field
    def update_expression(val):
        current_text = entry.get()
        entry.delete(0, tk.END)
        entry.insert(0, current_text + val)

    # Function to evaluate the expression and display the result
    def evaluate_expression():
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(0, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(0, "Error")

    # Function to clear the entry field
    def clear_entry():
        entry.delete(0, tk.END)

    # Creating the entry field for the calculator
    entry = tk.Entry(calc_window, width=16, font=('Arial', 24), borderwidth=2, relief="solid")
    entry.grid(row=0, column=0, columnspan=4)

    # Buttons for the calculator
    buttons = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
        ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ]

    for (text, row, col) in buttons:
        if text == '=':
            button = tk.Button(calc_window, text=text, command=evaluate_expression, width=5, height=2, font=('Arial', 18))
        else:
            button = tk.Button(calc_window, text=text, command=lambda t=text: update_expression(t), width=5, height=2, font=('Arial', 18))
        button.grid(row=row, column=col)

    # Clear button
    clear_button = tk.Button(calc_window, text='C', command=clear_entry, width=5, height=2, font=('Arial', 18))
    clear_button.grid(row=5, column=3)

# Main window
root = tk.Tk()
root.title("Main Window")

# Button to open the calculator
open_calc_button = tk.Button(root, text="Open Calculator", command=open_calculator, font=('Arial', 18 , 'bold'))
open_calc_button.pack(pady=20)

# Running the application
root.mainloop()
