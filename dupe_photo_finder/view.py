import tkinter as tk
from tkinter import ttk, Menu, scrolledtext, filedialog, messagebox, Label, Frame, font
import sys
import os


class MenuBar:

    def __init__(self, parent, controller, listbox_dupe_sets, status_bar):
        self.parent = parent
        self.controller = controller
        self.listbox_dupe_sets = listbox_dupe_sets
        self.status_bar = status_bar
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
            self.controller.add_directory_to_search(new_directory)
            self.status_bar.update_message("Directories to search: " + str(len(self.controller.directories_to_search)))

    def process_search_request(self):
        progress_window = ProgressWindow(self.parent)
        progress_window.update_message('Searching for files')
        self.status_bar.update_message('Searching for duplicates')
        try:
            duplicate_sets = self.controller.request_search(progress_window)
        except ValueError as e:
            messagebox.showerror('Error', str(e))
            print( str(e))
        finally:
            progress_window.close_window()

        self.status_bar.clear_message()
        if duplicate_sets and len(duplicate_sets)>0:
            for index in range(0, len(duplicate_sets)):
                self.listbox_dupe_sets.add_item_to_list(index)


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
        self.label.pack(padx=12, pady=12)
        self.progress_bar = ttk.Progressbar(self.window)
        self.progress_bar.pack(fill='x', padx=12, pady=12)
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

    def __init__(self, parent, listbox_of_files):
        self.parent = parent
        self.listbox_of_files = listbox_of_files
        self.listbox = tk.Listbox(parent, selectmode = 'browse', borderwidth=0, highlightthickness=0, background='grey')
        bold = tk.font.Font(weight='bold')
        self.listbox.config(font=bold)
        self.listbox.pack(side='top')

    def add_item_to_list(self, item):
        self.listbox.insert('end', item)
        self.parent.update_idletasks()


class ListboxFiles:

    def __init__(self, parent):
        self.parent = parent
        self.listbox = tk.Listbox(parent, selectmode = 'single', borderwidth=0, highlightthickness=0, background='Blue')
        self.listbox.pack(side='top')

    def add_item_to_list(self, item):
        self.listbox.insert('end', item)
        self.parent.update_idletasks()


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
        frame1 = Frame(self.gui, background="grey")
        frame2 = Frame(self.gui)
        frame3 = Frame(self.gui, background='Blue')
        frame1.grid(row=0, column=0, sticky="nsew")
        frame2.grid(row=0, column=1, sticky="nsew")
        frame3.grid(row=0, column=2, sticky="nsew")
        status_bar = StatusBar(self.gui)
        listbox_of_files = ListboxFiles(frame2)
        listbox_dupe_sets = ListsWithSets(frame1, listbox_of_files)
        MenuBar(self.gui, self.controller, listbox_dupe_sets, status_bar)
        self.gui.mainloop()
