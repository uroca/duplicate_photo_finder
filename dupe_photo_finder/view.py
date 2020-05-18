import tkinter as tk
from tkinter import ttk, Menu, scrolledtext, filedialog, messagebox, Label, Frame, font
import sys
import os


class MenuBar:

    def __init__(self, parent, controller):
        self.parent = parent
        self.controller = controller
        self.directories_to_search = []
        menu_bar = Menu(parent)
        self.create_actions_menu(menu_bar)
        self.parent.config(menu=menu_bar)

    def _quit(self):
        self.parent.quit()
        self.parent.destroy()
        sys.exit()

    def add_search_directory(self):
        new_directory = filedialog.askdirectory(title = 'What directory should I search for duplicate photos?')
        if new_directory:
            self.directories_to_search.append(new_directory)

    def process_search_request(self):
        progress_window = ProgressWindow(self.parent)
        progress_window.update_message('Searching for files')
        try:
            self.controller.request_search(self.directories_to_search, progress_window)
        except ValueError as e:
            messagebox.showerror('Error', str(e))
            print( str(e))
        finally:
            progress_window.close_window()

    def create_actions_menu(self, menu_bar):
        actions_menu = Menu(menu_bar, tearoff = False)
        actions_menu.add_command (label = 'Add Directory', command = self.add_search_directory)
        actions_menu.add_command (label = 'Search for duplicates', command = self.process_search_request)
        actions_menu.add_separator()
        actions_menu.add_command (label = 'Exit', command = self._quit)

        menu_bar.add_cascade(menu = actions_menu, label = 'Actions')


class StatusBar:

    def __init__(self, parent):
        self.message = tk.StringVar()
        self.label = ttk.Label(parent, relief=tk.SUNKEN, textvariable = self.message)
        self.label.grid(column = 0, row = 1, columnspan = 3, sticky = 'nesw')

    def update_message(self, message):
        self.message.set(message)

    def clear_message(self):
        self.message.set('')


class ProgressWindow:

    def __init__(self, parent):
        self.parent = parent
        self.window = tk.Toplevel()
        self.window.title('Request Progress')
        self.window.geometry('300x100')
        self.window.lift()
        self.label = tk.Label(self.window, text='')
        self.label.pack()
        self.progress_bar = ttk.Progressbar(self.window)
        self.progress_bar.pack()
        self.parent.update_idletasks()

    def update_message(self, message):
        self.label.configure(text = message)
        self.parent.update_idletasks()

    def clear_message(self):
        self.update_message('')
        self.parent.update_idletasks()

    def change_max_value_progress_bar(self, value):
        self.progress_bar['maximum'] = value
        self.parent.update_idletasks()

    def update_progress_bar(self, value):
        self.progress_bar['value'] = value
        self.parent.update_idletasks()

    def close_window(self):
        self.window.destroy()
        self.parent.update_idletasks()




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
        status_bar.clear_message()
        frame1 = Frame(self.gui, background="grey")
        frame2 = Frame(self.gui)
        frame3 = Frame(self.gui, background='Blue')
        frame1.grid(row=0, column=0, sticky="nsew")
        frame2.grid(row=0, column=1, sticky="nsew")
        frame3.grid(row=0, column=2, sticky="nsew")
        ListsWithSets(frame1)
        self.gui.mainloop()
