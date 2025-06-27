import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

# BMI history list
bmi_history = []


# Function to calculate BMI and categorize
def calculate_bmi():
    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get())

        if weight <= 0 or height <= 0:
            raise ValueError("Invalid input: Must be positive.")

        bmi = round(weight / (height ** 2), 2)
        bmi_history.append(bmi)

        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 25:
            category = "Normal"
        elif 25 <= bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        result_label.config(text=f"BMI: {bmi} ({category})")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers for weight and height.")


# Function to show BMI history graph
def show_graph():
    if not bmi_history:
        messagebox.showinfo("No Data", "No BMI records to display.")
        return

    plt.plot(bmi_history, marker='o', linestyle='-', color='green')
    plt.title("BMI Trend")
    plt.xlabel("Entry Number")
    plt.ylabel("BMI")
    plt.grid(True)
    plt.show()


# GUI setup
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("350x250")
root.resizable(False, False)

# Weight input
tk.Label(root, text="Enter Weight (kg):").pack(pady=5)
entry_weight = tk.Entry(root)
entry_weight.pack()

# Height input
tk.Label(root, text="Enter Height (m):").pack(pady=5)
entry_height = tk.Entry(root)
entry_height.pack()

# Buttons
tk.Button(root, text="Calculate BMI", command=calculate_bmi).pack(pady=10)
tk.Button(root, text="Show BMI Trend", command=show_graph).pack(pady=5)

# Result
result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack(pady=10)

# Run the GUI
root.mainloop() 