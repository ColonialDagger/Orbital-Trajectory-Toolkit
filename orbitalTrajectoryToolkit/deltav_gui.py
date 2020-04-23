import tkinter
from tkinter import messagebox
from .tools import calculations
from.tools import helpers


class deltav_gui:
    def __init__(self):  # Initializers variables, creates stage entry GUI

        # Configurable Headers
        self.input_headers = ["Stages",
                              "Label",
                              "Wet Mass (kg)",
                              "Dry Mass (kg)",
                              "Thrust Force (kN)",
                              "Thrust Rate (kg/s)"]
        self.output_headers = [""]
        self.inputs = {}  # Leave blank, replace by input field

        # Other Variables
        self.input_lf = None

        # Defines Toplevel if run in main
        self.window = tkinter.Toplevel()
        self.window.title("Delta-V Calculator")

        # Stages Selector
        tkinter.Label(self.window, text="Number of Stages").grid(row=0, column=0, padx=5, pady=2)
        self.stages = tkinter.Entry(self.window, width=8)
        self.stages.grid(row=0, column=1, padx=5, pady=2)
        tkinter.Button(
            self.window,
            text="Enter",
            command=self.input_frame
        ).grid(row=0, column=2, padx=5, pady=2)

        tkinter.mainloop()

    def input_frame(self):  # Creates input label frame to display entry table

        try:  # Used to catch ValueErrors in stage entry
            stages = helpers.positive_int(self.stages.get())
        except ValueError or TypeError:
            messagebox.showerror("Error", "Stage entry must be a positive integer")
            return

        try:  # Clears pre-existing label frames
            self.window.input_lf.grid_forget()
        except AttributeError:
            pass

        # Create input label frame
        self.window.input_lf = tkinter.LabelFrame(self.window, text="Inputs")
        self.window.input_lf.grid(row=1, column=0, columnspan=3, padx=5, pady=2)

        col = 0
        for i in self.input_headers:
            tkinter.Label(self.window.input_lf, text=i).grid(row=1, column=col, padx=5, pady=2)
            col += 1

        # Input Section
        counter = 0
        for row in range(stages):
            tkinter.Label(self.window.input_lf, text=str(row+1)).grid(row=row+2, column=0)
            for col in range(len(self.input_headers)-1):
                self.inputs[counter] = tkinter.Entry(self.window.input_lf, width=8)
                self.inputs[counter].grid(row=row+2, column=col+1)
                counter += 1

        tkinter.Button(self.window, text="Calculate", command=self.calculate)\
            .grid(row=2, column=0, columnspan=3, padx=5, pady=2, sticky="ew")

        return self

    def calculate(self):  # Gets inputs from entry field, sorts properly, and returns any calculable values for outputs
        input_values = []
        for i in self.inputs:  # Gets all inputs as strings or integers, as necessary
            if i % (len(self.input_headers) - 1) == 0:
                input_values.append(str(self.inputs[i].get()))
            elif self.inputs[i].get() is None:
                input_values.append(0)
            else:
                try:
                    input_values.append(int(self.inputs[i].get()))
                except ValueError:
                    input_values.append(0)

        # Finds input headers width to split array into rows
        n = len(self.input_headers)-1
        input_values = [input_values[i * n:(i + 1) * n] for i in range((len(input_values) + n - 1) // n)]

        return self
