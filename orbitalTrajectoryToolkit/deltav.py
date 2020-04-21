import tkinter
from tkinter import messagebox
from .tools import calculations


class deltav():
    def __init__(self):

        # Defines either new Tk or Toplevel if run in main or standalone
        if __name__ != "__main__":
            self.window = tkinter.Toplevel()
        else:
            self.window = tkinter.Tk()
        self.window.title("Delta-V Calculator")

        # Stages Selector
        tkinter.Label(self.window, text="Number of Stages").grid(row=0, column=0, padx=5, pady=2)
        stages = tkinter.Entry(self.window, width=8)
        stages.grid(row=0, column=1, padx=5, pady=2)
        tkinter.Button(self.window, text="Enter", command=lambda x=0: self.inputs(self.checknum(stages.get())))\
            .grid(row=0, column=2, padx=5, pady=2)

        tkinter.mainloop()

    # Input Headers
    def inputs(self, stages):
        try:
            self.window.grid_forget()
        except:
            pass

        lf_in = tkinter.LabelFrame(self.window, text="Inputs")
        lf_in.grid(row=1, column=0, columnspan=6)

        col = 0
        headers = ["Stages", "Label", "Wet Mass (kg)", "Dry Mass (kg)", "Thrust Force (kN)", "Thrust Rate (kg/s)"]
        for i in headers:
            tkinter.Label(lf_in, text=i).grid(row=1, column=col, padx=5, pady=2)
            col += 1

        # Input Section
        row = 2
        for stage in range(int(stages)):
            col = 0
            for i in headers:
                tkinter.Entry(lf_in, width=8).grid(row=row, column=col, padx=5, pady=2)
                col += 1
            row += 1


        # RESULTS GRID
        # tkinter.Label(self.window, text="Stages").grid(row=1, column=0, padx=5, pady=2)
        # tkinter.Label(self.window, text="Label").grid(row=1, column=1, padx=5, pady=2)
        # tkinter.Label(self.window, text="TWR").grid(row=1, column=2, padx=5, pady=2)
        # tkinter.Label(self.window, text="Atmo. ΔV").grid(row=1, column=3, padx=5, pady=2)
        # tkinter.Label(self.window, text="Atmo. Time").grid(row=1, column=4, padx=5, pady=2)
        # tkinter.Label(self.window, text="Vac. ΔV").grid(row=1, column=5, padx=5, pady=2)
        # tkinter.Label(self.window, text="Vac. Time").grid(row=1, column=6, padx=5, pady=2)

        # Inputs


        # # Wet Mass Inputs
        # tkinter.Label(self.window, text="Wet Mass").grid(row=0, column=0, padx=5, pady=2)
        # tkinter.Label(self.window, text="kg").grid(row=0, column=2, padx=5, pady=2)
        # self.window.winput = tkinter.Entry(self.window, width=10)
        # self.window.winput.grid(row=0, column=1, padx=5, pady=2)
        #
        # # Dry Mass Inputs
        # tkinter.Label(self.window, text="Dry Mass").grid(row=1, column=0, padx=5, pady=2)
        # tkinter.Label(self.window, text="kg").grid(row=1, column=2, padx=5, pady=2)
        # self.window.dinput = tkinter.Entry(self.window, width=10)
        # self.window.dinput.grid(row=1, column=1, padx=5, pady=2)
        #
        # # ISP/ExV Inputs
        # self.window.ispdrop = tkinter.StringVar()
        # self.window.ispdrop.set("Specific Impulse")  # Sets default selection
        # self.window.isp = tkinter.OptionMenu(
        #     self.window, self.window.ispdrop, "Specific Impulse", "Exhaust Velocity"  # CURRENTLY ONLY ISP
        # ).grid(row=2, column=0, padx=5, pady=2)
        # tkinter.Label(self.window, text="kg OR m/s").grid(row=2, column=2, padx=5, pady=2)
        # self.window.ispinput = tkinter.Entry(self.window, width=10)
        # self.window.ispinput.grid(row=2, column=1, padx=5, pady=2)
        #
        # # Run Button and Separator
        # tkinter.Button(self.window, text="Run", command=self.calculate).grid(row=3, column=1, padx=5, pady=2)
        # ttk.Separator(self.window, orient="horizontal").grid(row=4, columnspan=3, padx=5, pady=2, sticky='ew')
        #
        #
        # # Results
        # self.window.deltav = tkinter.Label(self.window, text="Delta-V").grid(row=5, column=0, padx=5, pady=2)
        # self.window.deltav = tkinter.Label(self.window, text="ΔV").grid(row=5, column=2, padx=5, pady=2)


    def checknum(self, n):
        try:
            return float(n)
        except ValueError:
            tkinter.messagebox.showerror(title="Error", message="All inputs must be numerical: Check values!")

    def calculate(self):
        try:
            wet = float(self.window.winput.get())
            dry = float(self.window.dinput.get())
            isp = float(self.window.ispinput.get())
        except ValueError:
            tkinter.messagebox.showerror(title="Error", message="All inputs must be numerical values!")

        # Check against unit in dropdown
        if self.window.ispdrop.get()[0] == 'E':
            deltav_value = calculations.deltav(wet, dry, isp, 1)  # Exhaust Velocity
        else:
            deltav_value = calculations.deltav(wet, dry, isp, 0)  # Exhaust Velocity
        tkinter.Label(self.window, text="               ").grid(row=5, column=1)  # Required to clear text
        tkinter.Label(self.window, text=str(round(deltav_value, 4))).grid(row=5, column=1)

if __name__ == "__main__":
    deltav()