import tkinter as tk


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
        self.slope_label = tk.Label(self.root, text="Enter slope value- J:", font=self.fnt, fg='black')
        # place label with a space of 10 px above and 10 px below label
        self.slope_label.pack(pady=10)

        # create Entry widget, input field for slope
        self.slope_entry = tk.Entry(self.root, font=self.fnt, width=20, bg='lightgreen', fg='blue')
        self.slope_entry.pack(fill='both', expand=1)
        self.slope_entry.focus_set()

        # Manning's n
        self.manning_label = tk.Label(self.root, text="Enter manning's n:", font=self.fnt, fg='black')
        self.manning_label.pack(pady=10)

        self.manning_entry = tk.Entry(self.root, font=self.fnt, width=20, bg='lightgreen', fg='blue')
        self.manning_entry.pack(fill='both', expand=1)

        # Flow Q
        self.flow_label = tk.Label(self.root, text="Enter flow- Q in m^3/s:", font=self.fnt, fg='black')
        self.flow_label.pack(pady=10)

        self.flow_entry = tk.Entry(self.root, font=self.fnt, width=20, bg='lightgreen', fg='blue')
        self.flow_entry.pack(fill='both', expand=1)

        # Width b
        self.width_label = tk.Label(self.root, text="Enter width- b in m:", font=self.fnt, fg='black')
        self.width_label.pack(pady=10)

        self.width_entry = tk.Entry(self.root, font=self.fnt, width=20, bg='lightgreen', fg='blue')
        self.width_entry.pack(fill='both', expand=1)


root = tk.Tk()
myapp = MyApp(root)
root.mainloop()