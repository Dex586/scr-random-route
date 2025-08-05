import random
import tkinter as tk
from tkinter import messagebox

from data.operators import operators
from data.trains import connect_t, waterline_t, airlink_t, metro_t, express_t
from data.stations_by_op import connect_s, waterline_s, airlink_s, metro_s, express_s

# Mapping operator names to trains and stations
train_map = {
    "connect": connect_t,
    "waterline": waterline_t,
    "airlink": airlink_t,
    "metro": metro_t,
    "express": express_t,
}

station_map = {
    "connect": connect_s,
    "waterline": waterline_s,
    "airlink": airlink_s,
    "metro": metro_s,
    "express": express_s,
}

def generate_random():
    selected = operator_var.get()
    if not selected:
        messagebox.showwarning("No Operator", "Please select an operator.")
        return

    trains = train_map.get(selected)
    stations = station_map.get(selected)

    if not trains or not stations:
        messagebox.showerror("Missing Data", f"No data found for '{selected}'.")
        return
    if len(stations) < 2:
        messagebox.showerror("Station Error", "Need at least 2 stations.")
        return

    train = random.choice(trains)
    start, end = random.sample(stations, 2)

    result = f"Operator: {selected.capitalize()}\nTrain: {train}\nRoute: {start} → {end}"
    result_label.config(text=result)

# GUI
root = tk.Tk()
root.title("SCR Train Randomizer")
root.geometry("400x300")

tk.Label(root, text="Select Operator", font=("Arial", 14)).pack(pady=10)

operator_var = tk.StringVar()

for op in operators:
    tk.Radiobutton(
        root,
        text=op.capitalize(),
        variable=operator_var,
        value=op,
        font=("Arial", 12)
    ).pack(anchor="w", padx=30)

tk.Button(
    root,
    text="Generate Random Route",
    command=generate_random,
    font=("Arial", 12)
).pack(pady=20)

result_label = tk.Label(root, text="", font=("Arial", 12), wraplength=350, justify="left")
result_label.pack()

root.mainloop()