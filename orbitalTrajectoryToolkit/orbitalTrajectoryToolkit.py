import tkinter
import tkinter.font
from orbitalTrajectoryToolkit.deltav import deltav


class ottGUI:  # Main GUI
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.resizable(width=False, height=False)
        self.window.title("Orbital Trajectory Toolkit (OTT)")

        headerstyle = tkinter.font.Font(family="Consolas", size=12)
        fontstyle = tkinter.font.Font(family="Consolas", size=9)

        # Vehicle Statistics
        lf_vic = tkinter.LabelFrame(self.window, text="Vehicle Statistics", font=headerstyle)
        lf_vic.pack()
        for string, command in [
            ["Delta-V Calculator", deltav],
            ["Thrust to Weight Ratio", lambda x=0: print("disabled")]
        ]:
            tkinter.Button(lf_vic, text=string, command=command, font=fontstyle).pack(fill="x", padx=5, pady=2)

        # Orbital Trajectory Simulations
        lf_tjc = tkinter.LabelFrame(self.window, text="Orbital Trajectory Simulations", font=headerstyle)
        lf_tjc.pack()
        for string, command in [
            ["Single Body Trajectory", lambda x=0: print("disabled")],
            ["Orbiting Moons Trajectory", lambda x=0: print("disabled")],
            ["N-Body Trajectory", lambda x=0: print("disabled")],
            ["Orbital Decay Trajectory", lambda x=0: print("disabled")]
        ]:
            tkinter.Button(lf_tjc, text=string, command=command, font=fontstyle).pack(fill="x", padx=5, pady=2)

        # Orbital Maneuver Calculators
        lf_orm = tkinter.LabelFrame(self.window, text="Orbital Maneuver Calculators", font=headerstyle)
        lf_orm.pack()
        for string, command in [
            ["Planetary Transfer", lambda x=0: print("disabled")],
            ["Hohmann Transfer", lambda x=0: print("disabled")],
            ["Bi-elliptic Transfer", lambda x=0: print("disabled")],
            ["Low Energy Transfer", lambda x=0: print("disabled")],
            ["Orbital Inclination Change", lambda x=0: print("disabled")],
            ["Space Rendezvous", lambda x=0: print("disabled")]
        ]:
            tkinter.Button(lf_orm, text=string, command=command, font=fontstyle).pack(fill="x", padx=5, pady=2)

        # Ascent Guidance
        lf_asc = tkinter.LabelFrame(self.window, text="Ascent Guidance", font=headerstyle)
        lf_asc.pack()
        for i in [
            ["Launch Trajectory Guidance", lambda x=0: print("disabled")],
            ["Max-Q Curve", lambda x=0: print("disabled")]
        ]:
            tkinter.Button(lf_asc, text=i[0], command=i[1], font=fontstyle).pack(fill="x", padx=5, pady=2)
        self.window.mainloop()


if __name__ == "__main__":
    ottGUI()
