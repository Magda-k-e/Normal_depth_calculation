import tkinter as tk
from tkinter import messagebox


class MyApp():
    def __init__(self, root):
        self.product_by = None
        self.product_qnj = None
        self.width = None
        self.fnt = 'Arial 30'
        root.title('Compute normal depth')
        self.root = root
        self.slope = None
        self.manning = None
        self.flow = None
        self.norm_dep = 1
        self.widgets()

    def widgets(self):
        # slope J
        # create label widget for slope
        self.slope_label = tk.Label(self.root, text="Enter slope value J:", font=self.fnt, fg='black')
        # place label with a space of 10 px above and 10 px below label
        self.slope_label.pack(pady=10)

        # create Entry widget, input field for slope
        self.slope_entry = tk.Entry(self.root, font=self.fnt, width=20, bg='lightgreen', fg='blue')
        self.slope_entry.pack(fill='both', expand=1)
        self.slope_entry.focus_set()

        # Manning's n
        self.manning_label = tk.Label(self.root, text="Enter Manning's n:", font=self.fnt, fg='black')
        self.manning_label.pack(pady=10)

        self.manning_entry = tk.Entry(self.root, font=self.fnt, width=20, bg='lightgreen', fg='blue')
        self.manning_entry.pack(fill='both', expand=1)

        # Flow Q
        self.flow_label = tk.Label(self.root, text="Enter flow Q in m^3/s:", font=self.fnt, fg='black')
        self.flow_label.pack(pady=10)

        self.flow_entry = tk.Entry(self.root, font=self.fnt, width=20, bg='lightgreen', fg='blue')
        self.flow_entry.pack(fill='both', expand=1)

        # Width b
        self.width_label = tk.Label(self.root, text="Enter width b in m:", font=self.fnt, fg='black')
        self.width_label.pack(pady=10)

        self.width_entry = tk.Entry(self.root, font=self.fnt, width=20, bg='lightgreen', fg='blue')
        self.width_entry.pack(fill='both', expand=1)

        # calculate button
        self.submit_button = tk.Button(self.root, text="Calculate", font=self.fnt, command=self.calculate_dep)
        self.submit_button.pack(pady=20)

        self.result_label = tk.Label(self.root, text="Calculated normal depth:", font=self.fnt, fg='green')
        self.result_label.pack(pady=10)

    def calculate_dep(self):
        # get each value entered in each Entry
        try:
            self.slope = float(self.slope_entry.get())
            self.manning = float(self.manning_entry.get())
            self.flow = float(self.flow_entry.get())
            self.width = float(self.width_entry.get())
        except ValueError:
            messagebox.showerror("invalid input")
            return

        self.product_qnj = self.flow * self.manning / self.slope ** (1 / 2)

        self.product_by = (self.width * self.norm_dep) * (
                (self.width * self.norm_dep) / (self.width + 2 * self.norm_dep)) ** (2 / 3)

        tolerance = 1e-2

        while abs(self.product_by - self.product_qnj) > tolerance:
            if self.product_by > self.product_qnj:
                self.norm_dep -= 0.005
            else:
                self.norm_dep += 0.005

            # calculate product_by with new normal depth
            self.product_by = (self.width * self.norm_dep) * (
                    (self.width * self.norm_dep) / (self.width + 2 * self.norm_dep)) ** (2 / 3)

            self.root.update_idletasks()

            self.result_label.config(text=f"Calculated normal depth:{self.norm_dep:.2f}")


root = tk.Tk()
myapp = MyApp(root)
root.mainloop()
