import tkinter as tk
from tkinter import ttk, Menu, scrolledtext, filedialog, messagebox
import sys
import os


class StatusBar:

    def __init__(self, gui):
        self.gui = gui


class Widgets:

    def __init__(self, gui, controller):
        self.controller = controller
        self.add_buttons(gui)
        self.directories_to_search = []


    def add_search_directory(self):
        new_directory = filedialog.askdirectory(title = 'What directory should I search for duplicate photos?')
        self.directories_to_search.append(new_directory)


    def add_buttons(self, gui):
        button_add_directory = ttk.Button(gui, text="Add Directory", command = self.add_search_directory)
        button_add_directory.grid(column=1, row=1)
        button_execute_search = ttk.Button(gui, text="Search for Duplicates", command = self.process_search_request)
        button_execute_search.grid(column=2, row=1)


    def process_search_request(self):
        try:
            self.controller.request_search(self.directories_to_search, None)
        except Exception as e:
            messagebox.showerror('Error', str(e))


class Parent:
    def __init__(self, controller):
        self.controller = controller
        self.gui = tk.Tk()
        self.gui.geometry('600x400+450+150')
        self.gui.title('Duplicate Photo Detector')
        Widgets(self.gui, self.controller)
        self.gui.mainloop()
