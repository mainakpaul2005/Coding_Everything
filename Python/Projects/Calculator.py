import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Blurred Calculator")
root.geometry("300x400")
root.configure(bg="#1E1E1E")

# Create a fake "blurred" effect by layering widgets
bg_frame = tk.Frame(root, bg="#2C2C2C", relief="solid", bd=3)
bg_frame.place(relx=0.5, rely=0.5, anchor="center", width=280, height=350)

# Entry widget
entry = tk.Entry(bg_frame, font=("Arial", 22), borderwidth=5, relief="ridge", justify="right", bg="#444", fg="white")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Functions
def on_click(button_text):
    entry.insert(tk.END, button_text)

def calculate():
    try:
        result = eval(entry.get())  # Evaluating expression
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))  # Displaying result
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def clear():
    entry.delete(0, tk.END)

# Buttons with modern styling
buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('+',4,2)
]

for text, row, col in buttons:
    btn = tk.Button(bg_frame, text=text, width=5, height=2, font=("Arial", 18), bg="#555", fg="white", command=lambda t=text: on_click(t))
    btn.grid(row=row, column=col, padx=5, pady=5)

# "=" button
equal_btn = tk.Button(bg_frame, text="=", width=5, height=2, font=("Arial", 18), bg="#FF9800", fg="white", command=calculate)
equal_btn.grid(row=4, column=3, padx=5, pady=5)

# "C" button
clear_btn = tk.Button(bg_frame, text="C", width=5, height=2, font=("Arial", 18), bg="#D32F2F", fg="white", command=clear)
clear_btn.grid(row=5, column=0, columnspan=4, pady=5)

# Run the application
root.mainloop()