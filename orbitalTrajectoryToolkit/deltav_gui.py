import tkinter
from tkinter import messagebox
from .tools import calculations
from.tools import helpers


class deltav_gui:
    def __init__(self):

        # Configurable Headers
        self.input_headers = ["Stages",
                              "Label",
                              "Wet Mass (kg)",
                              "Dry Mass (kg)",
                              "Thrust Force (kN)",
                              "Thrust Rate (kg/s)"]
        self.output_headers = [""]

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

    def input_frame(self):

        try:  # Used to catch ValueErrors in stage entry
            stages = helpers.positive_int(self.stages.get()) + 1
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
        row = 2
        for stage in range(int(stages)-1):
            tkinter.Label(self.window.input_lf, text=str(stage+1)).grid(row=row, column=0, padx=5, pady=2)
            col = 1
            for i in self.input_headers[1:]:
                self.window.input_values = tkinter.Entry(self.window.input_lf, width=8)
                self.window.input_values.grid(row=row, column=col, padx=5, pady=2)
                col += 1
            row += 1

        tkinter.Button(self.window, text="Calculate", command=self.calculate)\
            .grid(row=2, column=0, columnspan=3, padx=5, pady=2, sticky="ew")

        return self

    def calculate(self):
        print(str(self.window.input_values.get()))
        print("pong!")
        return self




#     # Input Headers
#     def inputs(self, stages):
#         print("/n/n/n/n")
#         dir(self.window.Toplevel)
#         lf_in = tkinter.LabelFrame(self.window, text="Inputs")
#         lf_in.grid_forget()
#         lf_in.grid(row=1, column=0, columnspan=6)
#
#         col = 0
#         headers = ["Stages", "Label", "Wet Mass (kg)", "Dry Mass (kg)", "Thrust Force (kN)", "Thrust Rate (kg/s)"]
#         for i in headers:
#             tkinter.Label(lf_in, text=i).grid(row=1, column=col, padx=5, pady=2)
#             col += 1
#
#         # Input Section
#         row = 2
#         for stage in range(int(stages)):
#             col = 0
#             for i in headers:
#                 tkinter.Entry(lf_in, width=8).grid(row=row, column=col, padx=5, pady=2)
#                 col += 1
#             row += 1
#         tkinter.Button(self.window, text="Calculate", command=lambda x=0: print(lf_in.get("t"))).grid(row=2, column=0, columnspan=6, sticky="ew")
#
#         print(self.window.lf_in)
#         return self
#
#     def outputs(self, stages, labels):
#         lf_out = tkinter.LabelFrame(self.window, text="Results")
#         lf_out.grid(row=3, column=0, columnspan=6)
#         print()
#         return self
#
#     def checknum(self, n):
#         try:
#             return float(n)
#         except ValueError:
#             tkinter.messagebox.showerror(title="Error", message="All inputs must be numerical: Check values!")
#
#     def calculate(self):
#         try:
#             wet = float(self.window.winput.get())
#             dry = float(self.window.dinput.get())
#             isp = float(self.window.ispinput.get())
#         except ValueError:
#             tkinter.messagebox.showerror(title="Error", message="All inputs must be numerical values!")
#
#         # Check against unit in dropdown
#         if self.window.ispdrop.get()[0] == 'E':
#             deltav_value = calculations.deltav(wet, dry, isp, 1)  # Exhaust Velocity
#         else:
#             deltav_value = calculations.deltav(wet, dry, isp, 0)  # Exhaust Velocity
#         tkinter.Label(self.window, atext="               ").grid(row=5, column=1)  # Required to clear text
#         tkinter.Label(self.window, text=str(round(deltav_value, 4))).grid(row=5, column=1)
#
#
# if __name__ == "__main__":
#     deltav()
