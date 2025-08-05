import tkinter as tk
import random

# Import data from submodules
from data.operators import Operators
from data.trains import Waterline_t, Connect_t, AirLink_t, Metro_t, Express_t
from data.stations_by_op import Connect_S, AirLink_S, Waterline_S, Metro_S, Express_S

# Mapping for operator data
train_map = {
    "Waterline": Waterline_t,
    "Connect": Connect_t,
    "AirLink": AirLink_t,
    "Metro": Metro_t,
    "Express": Express_t
}

station_map = {
    "Waterline": Waterline_S,
    "Connect": Connect_S,
    "AirLink": AirLink_S,
    "Metro": Metro_S,
    "Express": Express_S
}

class RandomizerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Train Journey Generator")
        self.root.geometry("500x400")

        tk.Label(root, text="Select an Operator", font=("Helvetica", 14)).pack(pady=10)

        self.selected_operator = tk.StringVar(value="")

        for op in Operators:
            tk.Radiobutton(root, text=op, variable=self.selected_operator, value=op).pack(anchor="w", padx=20)

        tk.Button(root, text="Generate Journey", command=self.generate).pack(pady=20)

        self.operator_label = tk.Label(root, text="", font=("Helvetica", 12))
        self.operator_label.pack()
        self.train_label = tk.Label(root, text="", font=("Helvetica", 12))
        self.train_label.pack()
        self.route_label = tk.Label(root, text="", font=("Helvetica", 12))
        self.route_label.pack()

    def generate(self):
        op = self.selected_operator.get()

        if not op:
            self.operator_label.config(text="❌ Please select an operator")
            self.train_label.config(text="")
            self.route_label.config(text="")
            return

        trains = train_map.get(op, [])
        stations = station_map.get(op, [])

        if not trains or not stations:
            self.operator_label.config(text=f"⚠️ Missing data for {op}")
            self.train_label.config(text="")
            self.route_label.config(text="")
            return

        train = random.choice(trains)
        station1, station2 = random.sample(stations, 2) if len(stations) >= 2 else (stations[0], stations[0])

        self.operator_label.config(text=f"Operator: {op}")
        self.train_label.config(text=f"Train: {train}")
        self.route_label.config(text=f"From {station1} → To {station2}")

if __name__ == "__main__":
    root = tk.Tk()
    app = RandomizerGUI(root)
    root.mainloop()
