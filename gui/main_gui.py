import tkinter as tk
from tkinter import messagebox

# Function for buttons
def analog_sim():
    messagebox.showinfo("Analog Simulation", "This will run analog circuits!")

def digital_sim():
    messagebox.showinfo("Digital Simulation", "This will run digital circuits!")

def ai_explain():
    messagebox.showinfo("AI Explanation", "This will show AI explanations!")

# Create main window
root = tk.Tk()
root.title("VLSI Buddy Tool")
root.geometry("400x350")

# Welcome Label
label = tk.Label(root, text="🚀 Welcome to VLSI Buddy Tool!", font=("Arial", 14))
label.pack(pady=20)

# Buttons
btn_analog = tk.Button(root, text="Analog Simulation", command=analog_sim, width=25, height=2)
btn_analog.pack(pady=10)

btn_digital = tk.Button(root, text="Digital Simulation", command=digital_sim, width=25, height=2)
btn_digital.pack(pady=10)

btn_ai = tk.Button(root, text="AI Explanation", command=ai_explain, width=25, height=2)
btn_ai.pack(pady=10)

# Run the window
root.mainloop()
