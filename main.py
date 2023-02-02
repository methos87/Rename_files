#! /usr/bin/env python

import os
import re
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog


class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Renamer")
        self.wm_iconbitmap(default='img/icon.ico')
        self.resizable(False, False)
        self.st_font = 'Arial', 10
        self.bold_font = 'Arial', 10, 'bold'

        self.folder_path = tk.StringVar()
        self.files = []
        self.add_txt = tk.StringVar()

        self.window_width = 800
        self.window_height = 525

        self.geometry("{}x{}".format(self.window_width, self.window_height))

        # Get the screen width and height
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Calculating x and y coordinates for the window
        x = int((screen_width / 2) - (self.window_width / 2))
        y = int((screen_height / 2) - (self.window_height / 2))

        # Set the dimensions of the screen and where it is placed
        self.geometry('{}x{}+{}+{}'.format(self.window_width, self.window_height, x, y))

        # Create the menu bar
        menu_bar = tk.Menu(self)
        self.config(menu=menu_bar)

        # Create a File menu and add it to the menu bar
        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", underline=0, menu=file_menu)
        file_menu.add_command(label="Open...", command=self.open_folder)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.quit)

        # Create a File menu and add it to the menu bar
        about_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Help", menu=about_menu)
        about_menu.add_command(label="Help", command=self.help)
        about_menu.add_command(label="About", command=self.about)

        # ------------------------------LEFT FRAME---------------------------------------
        # Creating the Directory frame
        left_frame = tk.LabelFrame(self, text="Directory", bg="white", fg="black")
        left_frame.grid(row=0, column=0, sticky="nswe", padx=5)

        # Creating an entry field for path
        e1 = tk.Entry(left_frame, width=50, textvariable=self.folder_path)
        e1.grid(row=0, column=0, padx=5, pady=10)

        # Create a browser button
        b1 = tk.Button(left_frame, text="Browse", width=10, command=lambda: browse_button())
        b1.grid(row=0, column=1, padx=5, pady=10, sticky="N")

        # Create an entry field for input text
        tk.Label(left_frame, text='Add: ').grid(row=4, column=0, sticky="W", padx=10)
        e1 = tk.Entry(left_frame, width=50, textvariable=self.add_txt)
        e1.grid(row=5, column=0, sticky="W", padx=10)

        # Create an add button
        b1 = tk.Button(left_frame, text="Add", width=10, command=lambda: add(self.add_txt))
        b1.grid(row=5, column=1, padx=5, sticky="N")

        # Create a remove button
        b1 = tk.Button(left_frame, text="Remove", width=10, command=lambda: remove(self.add_txt))
        b1.grid(row=8, column=1, padx=5, sticky="N")

        # ------------------------------RIGHT FRAME---------------------------------------
        # Creating the right frame
        right_frame = tk.LabelFrame(self, text="Files", bg="white", fg="black")
        right_frame.grid(row=0, column=1, sticky="nswe")

        # Creating an entry field for show files
        self.e3 = tk.Text(right_frame, font=self.st_font, width=40)
        self.e3.grid(row=0, column=0, padx=10, pady=10, ipadx=10, ipady=40)

        # # Create a button 2
        # b2 = tk.Button(self, text="Add", command=add(file_path, "text"))
        # b2.grid(row=4, column=1)

    @staticmethod
    def open_folder():
        browse_button()

    @staticmethod
    def help():
        messagebox.showinfo("showinfo", "This is a help...")

    @staticmethod
    def about():
        messagebox.showinfo("showinfo", "Version is v.0")


def add(text):
    my_text = str(text.get())
    file_path = str(window.folder_path.get()) + "/"
    print("Adding \"{}\" to {}".format(my_text, file_path))

    for filename in os.listdir(file_path):
        print(filename)
        dst = my_text + filename
        src = file_path + filename
        dst = file_path + dst
        os.rename(src, dst)
    print_out()


def remove(text):
    my_text = str(text.get())
    file_path = str(window.folder_path.get()) + "/"
    count = 0
    print("Removing \"{}\" from {}".format(my_text, file_path))

    # for filename in window.files:
    #     if re.search(my_text, filename):
    #         print("Text is removed!")
    #         count += 1

    for filename in os.listdir(file_path):
        if re.search(my_text, filename):
            dst = filename.replace(my_text, '')
            src = file_path + filename
            dst = file_path + dst
            os.rename(src, dst)
            count += 1

    write_out()

    if count == 0:
        messagebox.showinfo("showinfo", "The given text is not found in the list!")
    else:
        messagebox.showinfo("showinfo", "Text is removed!")


def browse_button():
    folder_name = filedialog.askdirectory()
    window.folder_path.set(folder_name)
    print(folder_name)
    for filename in os.listdir(folder_name):
        window.files.append(filename)
    write_out()
    print_out()


def write_out():
    window.files.clear()
    window.e3.delete("1.0", "end")
    for names in window.files:
        window.e3.insert("end", names + '\n')
    window.e3.config(state="disabled")


def print_out():
    for names in window.files:
        print(names)


if __name__ == '__main__':
    try:
        window = Window()
        window.mainloop()
    except NameError:
        print("Error 0x000")
        messagebox.showinfo("showinfo", "Error 0x000")
    except FileNotFoundError:
        print("Filepath is not correct!")
        messagebox.showinfo("showinfo", "Filepath is not correct!")
    except KeyboardInterrupt:
        print("User terminated the software!")
