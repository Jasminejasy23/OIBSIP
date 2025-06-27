import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

def generate_password():
    length = length_var.get()

    if not (uppercase_var.get() or lowercase_var.get() or numbers_var.get() or symbols_var.get()):
        messagebox.showwarning("Invalid Input", "Select at least one character type.")
        return

    if length < 4:
        messagebox.showwarning("Invalid Length", "Password length should be at least 4.")
        return

    characters = ""
    if uppercase_var.get():
        characters += string.ascii_uppercase
    if lowercase_var.get():
        characters += string.ascii_lowercase
    if numbers_var.get():
        characters += string.digits
    if symbols_var.get():
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    result_entry.delete(0, tk.END)
    result_entry.insert(0, password)

def copy_to_clipboard():
    password = result_entry.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("No Password", "Please generate a password first.")

# GUI setup
root = tk.Tk()
root.title("Random Password Generator")
root.geometry("400x350")
root.resizable(False, False)

# Title
tk.Label(root, text="Password Generator", font=("Helvetica", 16, "bold")).pack(pady=10)

# Password length
tk.Label(root, text="Password Length:").pack()
length_var = tk.IntVar(value=12)
tk.Spinbox(root, from_=4, to=64, textvariable=length_var, width=5).pack(pady=5)

# Checkboxes for character types
uppercase_var = tk.BooleanVar(value=True)
lowercase_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include Uppercase Letters", variable=uppercase_var).pack(anchor='w', padx=20)
tk.Checkbutton(root, text="Include Lowercase Letters", variable=lowercase_var).pack(anchor='w', padx=20)
tk.Checkbutton(root, text="Include Numbers", variable=numbers_var).pack(anchor='w', padx=20)
tk.Checkbutton(root, text="Include Symbols", variable=symbols_var).pack(anchor='w', padx=20)

# Generate button
tk.Button(root, text="Generate Password", command=generate_password, bg="green", fg="white").pack(pady=10)

# Result entry
result_entry = tk.Entry(root, font=("Helvetica", 12), width=30, justify='center')
result_entry.pack(pady=5)

# Copy to clipboard
tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard).pack(pady=5)

# Run the GUI
root.mainloop()