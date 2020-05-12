import tkinter as tk
from tkinter import ttk, Menu, scrolledtext
import sys


class StatusBar:

    def __init__(self, gui):
        self.gui = gui


class Widgets:

    def __init__(self, gui):
        self.gui = gui
        self.button_add_directory = None
        self.button_execute_search = None
        self.add_buttons()

    def add_buttons(self):
        self.button_add_directory = ttk.Button(self.gui, text="Add Directory")
        self.button_add_directory.grid(column=1, row=1)
        self.button_execute_search = ttk.Button(self.gui, text="Search for Duplicates")
        self.button_execute_search.grid(column=2, row=1)


if __name__ == "__main__":
    gui = tk.Tk()
    gui.geometry('600x400+450+150')
    gui.title('Duplicate Photo Detector')
    widgets = Widgets(gui)
    gui.mainloop()