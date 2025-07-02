import tkinter as tk
from tkinter import messagebox
import numpy as np
import joblib
import winsound

# Load trained model and scaler
model = joblib.load("fall_model_6feat.pkl") 
scaler = joblib.load("scaler_6feat.pkl")

# Prediction Function
def detect_fall():
    try:
        # Read and convert values from input fields
        values = [float(entry.get()) for entry in entries]
        values_np = np.array(values).reshape(1, -1)

        # Scale and predict
        values_scaled = scaler.transform(values_np)
        prediction = model.predict(values_scaled)[0]

        # Show result
        if prediction == 1:
            winsound.Beep(2500, 1000)
            messagebox.showwarning("ALERT", "FALL DETECTED! Immediate attention needed.")
        else:
            messagebox.showinfo("Result", "No fall detected.")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numeric sensor values.")

# GUI Setup
root = tk.Tk()
root.title("Fall Detection Input - 10 Features")
root.geometry("400x550")

tk.Label(root, text="Enter 10 Sensor Values", font=("Arial", 16, "bold")).pack(pady=10)

# Entry fields
entries = []
labels = ["AX1", "AY1", "AZ1", "RX1", "RY1", "RZ1", "AX2", "AY2", "AZ2", "RX2"]

for label in labels:
    frame = tk.Frame(root)
    frame.pack(pady=4)
    tk.Label(frame, text=label + ":", width=10).pack(side=tk.LEFT)
    e = tk.Entry(frame)
    e.pack(side=tk.LEFT)
    entries.append(e)

# Detect Button
btn = tk.Button(root, text="Detect Fall", command=detect_fall, bg="blue", fg="white", font=("Arial", 12, "bold"))
btn.pack(pady=20)

root.mainloop()

'''
AX1:  -2.25  
AY1: -10.74  
AZ1:   2.41  
RX1:  -0.05  
RY1:  -0.59  
RZ1:  -0.06  
AX2:   0.84  
AY2: -10.53  
AZ2:   2.31  
RX2:   1.64

'''