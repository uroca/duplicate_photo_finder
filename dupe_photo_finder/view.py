import tkinter as tk
from tkinter import ttk, Menu, scrolledtext, filedialog, messagebox, Label, Frame, font
import sys
import os
import platform


class MenuBar:

    def __init__(self, parent):
        self.parent = parent
        menu_bar = Menu(self.parent.gui)
        self.create_actions_menu(menu_bar)
        self.create_results_menu(menu_bar)
        self.create_help_menu(menu_bar)
        self.parent.gui.config(menu=menu_bar)

    def _quit(self):
        self.parent.quit()

    def add_search_directory(self):
        new_directory = filedialog.askdirectory(title = 'What directory should I search for duplicate photos?')
        if new_directory:
            self.parent.controller.add_directory_to_search(new_directory)
            self.parent.status_bar.update_message("Directories to search: " + str(len(self.parent.controller.directories_to_search)))

    def process_search_request(self):
        progress_window = ProgressWindow(self.parent)
        progress_window.update_message('Searching for files')
        self.parent.status_bar.update_message('Searching for duplicates')
        try:
            duplicate_sets = self.parent.controller.request_search(progress_window)
        except ValueError as e:
            messagebox.showerror('Error', str(e))
            print( str(e))
        finally:
            progress_window.close_window()

        self.parent.status_bar.clear_message()
        if duplicate_sets and len(duplicate_sets)>0:
            for index in range(0, len(duplicate_sets)):
                self.parent.listbox_dupe_sets.add_item_to_list(index)


    @staticmethod
    def feature_not_done_window():
        not_done_window = tk.messagebox.showinfo(title="This feature isn't finished",
                                                 message="We're working on it!")

    def create_actions_menu(self, menu_bar):
        actions_menu = Menu(menu_bar, tearoff = False)
        actions_menu.add_command (label = 'Add Directory', command = self.add_search_directory)
        actions_menu.add_command (label = 'Search for duplicates', command = self.process_search_request)
        actions_menu.add_separator()
        actions_menu.add_command (label = 'Exit', command = self._quit)
        menu_bar.add_cascade(menu=actions_menu, label='Actions')

    def create_results_menu(self, menu_bar):
        results_menu = Menu(menu_bar, tearoff=False)
        results_menu.add_command(label='Save the results', command=MenuBar.feature_not_done_window)
        results_menu.add_command(label='Load the results', command=MenuBar.feature_not_done_window)
        menu_bar.add_cascade(menu=results_menu, label='Results')

    def create_help_menu(self, menu_bar):
        help_menu = Menu(menu_bar, tearoff=False)
        help_menu.add_command(label='How does it work', command=MenuBar.feature_not_done_window)
        help_menu.add_command(label='About', command=MenuBar.feature_not_done_window)
        menu_bar.add_cascade(menu=help_menu, label='Help')


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
        self.parent.gui.update_idletasks()

    def update_message(self, message):
        self.label.configure(text = message)
        self.parent.gui.update_idletasks()

    def clear_message(self):
        self.update_message('')
        self.parent.gui.update_idletasks()

    def change_max_value_progress_bar(self, value):
        self.progress_bar['maximum'] = value
        self.parent.gui.update_idletasks()

    def update_progress_bar(self, value):
        self.progress_bar['value'] = value
        self.parent.gui.update_idletasks()

    def close_window(self):
        self.window.destroy()
        self.parent.gui.update_idletasks()


class ListsWithSets:

    def __init__(self, parent):
        self.parent = parent
        self.label = ttk.Label(self.parent.frame1, text='Groups of duplicate photos')
        self.label.pack(side='top')
        self.listbox = tk.Listbox(self.parent.frame1, selectmode = 'browse', borderwidth=0, highlightthickness=0, background='grey')
        bold = tk.font.Font(weight='bold')
        self.listbox.config(font=bold)
        self.listbox.pack(side='top')

        def cursor_selection(evt):
            value = self.listbox.curselection()[0]
            self.parent.treeview_of_files.display_duplicate_group(value)

        self.listbox.bind('<<ListboxSelect>>', cursor_selection)

    def add_item_to_list(self, item):
        self.listbox.insert('end', item)
        self.parent.frame1.update_idletasks()


class TreeviewFiles:

    def __init__(self, parent):
        self.parent = parent
        self.label = ttk.Label(self.parent.frame2, text='Location of the duplicate photos')
        self.label.pack(side='top')
        self.treeview = ttk.Treeview(self.parent.frame2, show='tree headings')
        self.treeview.pack(side='top', fill='both')
        self.treeview['columns'] = ("action")
        self.treeview.heading("#0", text="Name")
        self.treeview.heading("action", text="Action")
        self.treeview.column("#0", anchor='w', stretch=tk.YES, width = 150, minwidth= 80)
        self.treeview.column("action",  anchor='e', stretch=tk.NO, width = 70, minwidth= 70)

    def display_duplicate_group(self, duplicate_group_number):
        self.clear_treeview()
        relative_paths = self.parent.controller.get_paths_of_set_of_duplicates(duplicate_group_number)
        for r in relative_paths:
            self.treeview.insert(r.parent, 'end', iid=r.index, text=r.text, open = True)
        self.parent.gui.update_idletasks()

    def clear_treeview(self):
        for row in self.treeview.get_children():
            self.treeview.delete(row)


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

        self.frame1 = Frame(self.gui, background="grey")
        self.frame2 = Frame(self.gui)
        self.frame3 = Frame(self.gui, background='Blue')
        self.frame1.grid(row=0, column=0, sticky="nsew")
        self.frame2.grid(row=0, column=1, sticky="nsew")
        self.frame3.grid(row=0, column=2, sticky="nsew")

        self.status_bar = StatusBar(self.gui)
        self.treeview_of_files = TreeviewFiles(self)
        self.listbox_dupe_sets = ListsWithSets(self)
        self.menu_bar = MenuBar(self)

        self.gui.mainloop()

    def quit(self):
        self.gui.quit()
        self.gui.destroy()
        sys.exit()
