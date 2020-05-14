import tkinter as tk
from tkinter import ttk, Menu, scrolledtext, filedialog, messagebox, Label, Frame, font
import sys
import os


class MenuBar:

    def __init__(self, gui, controller):
        gui = gui
        self.controller = controller
        self.directories_to_search = []
        menu_bar = Menu(gui)
        self.create_actions_menu(menu_bar)
        gui.config(menu=menu_bar)

    def _quit(self):
        self.gui.quit()
        self.gui.destroy()
        sys.exit()

    def add_search_directory(self):
        new_directory = filedialog.askdirectory(title = 'What directory should I search for duplicate photos?')
        if new_directory:
            self.directories_to_search.append(new_directory)

    def process_search_request(self):
        try:
            self.controller.request_search(self.directories_to_search, None)
        except Exception as e:
            messagebox.showerror('Error', str(e))

    def create_actions_menu(self, menu_bar):
        actions_menu = Menu(menu_bar, tearoff = False)
        actions_menu.add_command (label = 'Add Directory', command = self.add_search_directory)
        actions_menu.add_command (label = 'Search for duplicates', command = self.process_search_request)
        actions_menu.add_separator()
        actions_menu.add_command (label = 'Exit', command = self._quit)

        menu_bar.add_cascade(menu = actions_menu, label = 'Actions')


class StatusBar:

    def __init__(self, parent):
        self.label = ttk.Label(parent, relief=tk.SUNKEN)
        self.label.grid(column = 0, row = 1, columnspan = 3, sticky = 'nesw')

    def update_message(self, message):
        self.label.config(text = message)


class ListsWithSets:

    def __init__(self, parent):
        self.listbox = tk.Listbox(parent, borderwidth=0, highlightthickness=0, background="grey")
        bold = tk.font.Font(weight='bold')
        self.listbox.config(font=bold)
        self.listbox.insert('end','Item 2')
        self.listbox.pack(side='top')


class Parent:
    def __init__(self, controller):
        self.controller = controller
        self.gui = tk.Tk()
        self.gui.geometry('1000x720+80+80')
        self.gui.title('Duplicate Photo Detector')
        self.gui.grid_rowconfigure(0, weight=100)
        self.gui.grid_rowconfigure(1, weight=1)
        self.gui.grid_columnconfigure(0, weight=1)
        self.gui.grid_columnconfigure(1, weight=6)
        self.gui.grid_columnconfigure(2, weight=6)
        MenuBar(self.gui, self.controller)
        status_bar = StatusBar(self.gui)
        status_bar.update_message('Here it is!')

        frame1 = Frame(self.gui, background="grey")
        frame2 = Frame(self.gui)
        frame3 = Frame(self.gui, background='Blue')
        frame1.grid(row=0, column=0, sticky="nsew")
        frame2.grid(row=0, column=1, sticky="nsew")
        frame3.grid(row=0, column=2, sticky="nsew")
        ListsWithSets(frame1)
        self.gui.mainloop()
