import ltspice
import matplotlib.pyplot as plt
from tkinter import messagebox

# Function for buttons
def analog_sim():
   try:
        # Load the raw file
        l = ltspice.Ltspice("analog/divider.raw")
        l.parse()  # parse simulation results
        
        # Extract time and output voltage
        time = l.get_time()
        vout = l.get_data('Vout')  # replace 'Vout' with your node name
        
        # Plot waveform
        plt.plot(time, vout)
        plt.title("Analog Simulation: Divider Circuit")
        plt.xlabel("Time (s)")
        plt.ylabel("Voltage (V)")
        plt.grid(True)
        plt.show()
    except Exception as e:
        messagebox.showerror("Error", f"Cannot run simulation:\n{e}")
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

