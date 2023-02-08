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
        self.radio = tk.IntVar()
        self.st_font = 'Arial', 10
        self.bold_font = 'Arial', 10, 'bold'
        self.button_width = 8

        self.folder_path = tk.StringVar()
        self.files = []
        self.add_txt = tk.StringVar()

        self.window_width = 675
        self.window_height = 500

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
        menu_bar = tk.Menu(self, bg="black")
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

        # ------------------------------TOP FRAME---------------------------------------
        # Creating the Directory frame
        top_frame = tk.LabelFrame(self, text="Describing")
        top_frame.grid(row=0, column=0, sticky="W", padx=5, ipadx=284)

        # Creating an entry field for path
        tk.Label(top_frame, text='Describe texting').grid(row=4, column=0, sticky="W")

        # ------------------------------BOTTOM FRAME---------------------------------------

        # Creating the Directory frame
        bottom_frame = tk.LabelFrame(self, text="Settings")
        bottom_frame.grid(row=1, column=0, sticky="W", padx=5)

        # ------------------------------LEFT FRAME---------------------------------------
        # Creating the Directory frame
        left_frame = tk.LabelFrame(bottom_frame, text="Directory", fg="black")
        left_frame.grid(row=1, column=0, sticky="NSWE", padx=5, pady=5)

        # Creating an entry field for path
        e1 = tk.Entry(left_frame, width=40, textvariable=self.folder_path)
        e1.grid(row=0, column=0, padx=5, pady=10)

        # Create a browser button
        b1 = tk.Button(left_frame, text="Browse", width=self.button_width, command=lambda: browse_button())
        b1.grid(row=0, column=1, padx=5, pady=10, sticky="N")

        # Create an entry field for input text
        tk.Label(left_frame, text='Add: ').grid(row=4, column=0, sticky="W", padx=10)
        e1 = tk.Entry(left_frame, width=40, textvariable=self.add_txt)
        e1.grid(row=5, column=0, sticky="W", padx=10)

        # Create an add button
        b1 = tk.Button(left_frame, text="Add", width=self.button_width, command=lambda: add(self.add_txt))
        b1.grid(row=5, column=1, padx=5, sticky="N")

        # Create a radio buttons for first and after
        r1 = tk.Radiobutton(left_frame, text="Add to first", variable=self.radio, value=1)
        r1.grid(row=8, column=0, padx=10, sticky="W")

        r2 = tk.Radiobutton(left_frame, text="Add to last", variable=self.radio, value=2)
        r2.grid(row=9, column=0, padx=10, sticky="W")

        # Create a remove button
        b1 = tk.Button(left_frame, text="Remove", width=self.button_width, command=lambda: remove(self.add_txt))
        b1.grid(row=8, column=1, padx=5)

        # ------------------------------RIGHT FRAME---------------------------------------
        # Creating the right frame
        right_frame = tk.LabelFrame(bottom_frame, text="Files", fg="black")
        right_frame.grid(row=1, column=1, sticky="NSWE", padx=5, pady=5)

        # Creating an entry field for show files
        self.e3 = tk.Text(right_frame, font=self.st_font, width=38)
        self.e3.grid(row=0, column=0, padx=10, pady=10)

    @staticmethod
    def open_folder():
        browse_button()

    @staticmethod
    def help():
        messagebox.showinfo("showinfo", "This is a small application for renaming files. Enjoy!")

    @staticmethod
    def about():
        messagebox.showinfo("showinfo", "Version is v.0")


def add(text):
    my_text = str(text.get())
    file_path = str(window.folder_path.get()) + "/"
    print("Adding \"{}\" to {}".format(my_text, file_path))

    for filename in os.listdir(file_path):
        print(filename)
        res = re.search(r'\.[a-z]{1,3}', filename)
        st = res.start()
        dst = ""
        print(st)

        # adding first
        if window.radio.get() == 1:
            dst = my_text + filename

        # adding last
        elif window.radio.get() == 2:
            dst = list(filename)
            dst.insert(st, my_text)
            dst = ''.join(dst)

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
        messagebox.showinfo("showinfo", "{} is removed!".format(my_text))


def browse_button():
    folder_name = filedialog.askdirectory()
    window.folder_path.set(folder_name)
    print(folder_name)
    for filename in os.listdir(folder_name):
        window.files.append(filename)
    write_out()
    print_out()


def write_out():
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
