import tkinter as tk

# Create main window
root = tk.Tk()
root.title("VLSI Buddy Tool")
root.geometry("400x300")

# Add a welcome label
label = tk.Label(root, text="🚀 Welcome to VLSI Buddy Tool!", font=("Arial", 14))
label.pack(pady=20)

# Run the window
root.mainloop()
