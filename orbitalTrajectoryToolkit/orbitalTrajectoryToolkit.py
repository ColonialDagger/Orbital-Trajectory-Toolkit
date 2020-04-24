import tkinter
import tkinter.font
from orbitalTrajectoryToolkit.deltav_gui import deltav_gui


class ottGUI:  # Main GUI
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.resizable(width=False, height=False)
        self.window.title("Orbital Trajectory Toolkit (OTT)")

        headerstyle = tkinter.font.Font(family="Consolas", size=12)
        fontstyle = tkinter.font.Font(family="Consolas", size=9)

        # Vehicle Statistics
        lf_vic = tkinter.LabelFrame(self.window, text="Vehicle Information", font=headerstyle)
        lf_vic.pack(padx=5, pady=2)
        for string, command, state in [
            ["ΔV/TWR/ΔT Calculator", deltav_gui, "normal"]
        ]:
            tkinter.Button(lf_vic, text=string, command=command, state=state, font=fontstyle)\
                .pack(fill="x", padx=5, pady=2)

        # Orbital Trajectory Simulations
        lf_tjc = tkinter.LabelFrame(self.window, text="Orbital Trajectory Simulations", font=headerstyle)
        lf_tjc.pack(padx=5, pady=2)
        for string, command, state in [
            ["Single Body Trajectory", (), "disabled"],
            ["Orbiting Moons Trajectory", (), "disabled"],
            ["N-Body Trajectory", (), "disabled"],
            ["Orbital Decay Trajectory", (), "disabled"]
        ]:
            tkinter.Button(lf_tjc, text=string, command=command, state=state, font=fontstyle)\
                .pack(fill="x", padx=5, pady=2)

        # Orbital Maneuver Calculators
        lf_orm = tkinter.LabelFrame(self.window, text="Orbital Maneuver Calculators", font=headerstyle)
        lf_orm.pack(padx=5, pady=2)
        for string, command, state in [
            ["Planetary Transfer", (), "disabled"],
            ["Hohmann Transfer", (), "disabled"],
            ["Bi-elliptic Transfer", (), "disabled"],
            ["Low Energy Transfer", (), "disabled"],
            ["Orbital Inclination Change", (), "disabled"],
            ["Space Rendezvous", (), "disabled"]
        ]:
            tkinter.Button(lf_orm, text=string, command=command, state=state, font=fontstyle)\
                .pack(fill="x", padx=5, pady=2)

        # Ascent Guidance
        lf_asc = tkinter.LabelFrame(self.window, text="Ascent Guidance", font=headerstyle)
        lf_asc.pack(padx=5, pady=2)
        for string, command, state in [
            ["Launch Trajectory Guidance", lambda x=0: print("disabled"), "disabled"],
            ["Max-Q Curve", lambda x=0: print("disabled"), "disabled"]
        ]:
            tkinter.Button(lf_asc, text=string, command=command, state=state, font=fontstyle)\
                .pack(fill="x", padx=5, pady=2)

        self.window.mainloop()


if __name__ == "__main__":
    ottGUI()
