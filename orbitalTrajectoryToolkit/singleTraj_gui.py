import tkinter
import tkinter.font
import pygame
import datetime


class singleTraj_gui:
    def __init__(self):

        # Configs
        planets = [
            "Earth",
            "Moon",
            "Venus",
            "Mars"
        ]

        headerstyle = tkinter.font.Font(family="Consolas", size=12)
        fontstyle = tkinter.font.Font(family="Consolas", size=9)

        # Window
        window = tkinter.Toplevel()
        window.title("Single Body Trajectory")
        window.resizable(width=False, height=False)

        # Label Frames
        bodylf = tkinter.LabelFrame(window, text="Planetary Information", font=headerstyle)
        bodylf.grid(row=0, column=0, columnspan=2, padx=5, pady=2)
        timelf = tkinter.LabelFrame(window, text="Time Settings", font=headerstyle)
        timelf.grid(row=1, column=0, columnspan=2, padx=5, pady=2)
        vehiclelf = tkinter.LabelFrame(window, text="Vehicle", font=headerstyle)
        vehiclelf.grid(row=2, column=0, columnspan=2, padx=5, pady=2)

        # Body Settings
        body_clicked = tkinter.StringVar()
        body_clicked.set(planets[0])
        body = tkinter.OptionMenu(bodylf, body_clicked, *planets)
        body.config(width=10)
        body.grid(row=0, column=0, padx=5, pady=2, sticky="ew")

        # Time Settings
        tkinter.Label(timelf, text="Start Time", font=fontstyle).grid(row=0, column=0)
        tkinter.Entry(timelf, text="Placeholder", font=fontstyle).grid(row=1, column=0)  # TODO: Replace with datetime input
        tkinter.Label(timelf, text=" ").grid(row=2, column=0)  # Spacer
        tkinter.Label(timelf, text="End Time", font=fontstyle).grid(row=3, column=0)

        r = tkinter.IntVar()
        tkinter.Radiobutton(timelf, text="Current time", variable=r, value=0, font=fontstyle).grid(row=4, column=0)
        tkinter.Radiobutton(timelf, text="Custom time", variable=r, value=1, font=fontstyle).grid(row=4, column=1)

        start_date = datetime.datetime.now()

        print(body_clicked.get())

        window.mainloop()

        return

    def sim(self, body):
        pass
        # TODO: Create 3D Simulation
