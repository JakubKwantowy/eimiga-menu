#!/bin/env python3

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog
import os
import multiprocessing

root = None 
icon = None

print("+-------------+")
print("| EIMIGA MENU |")
print("+-------------+")

def close():
    answer = messagebox.askyesnocancel("Eimiga Menu", "Would you like to hide Eimiga Menu instead of closing?")
    if answer is None: return
    if answer: root.iconify()
    else: root.destroy()

def run():
    to_run = simpledialog.askstring("Eimiga Menu", "Command: ")
    if not to_run: return
    t = multiprocessing.Process(target=lambda:os.system("gnome-terminal -- "+to_run))
    t.start()

def bash():
    t = multiprocessing.Process(target=lambda:os.system("gnome-terminal /bin/bash"))
    t.start()

def main():
    global root
    global icon
    root = tk.Tk()
    root.title("Eimiga Menu")
    root.geometry("640x0")
    root.config(background="#0080C0")
    icon = tk.PhotoImage(file="favicon.png")
    root.iconphoto(True, icon)
    root.resizable(False, False) 
    root.protocol('WM_DELETE_WINDOW', close)

    menubar = tk.Menu(root)
    file_menu = tk.Menu(menubar)
    file_menu.add_command(
        label='Run',
        command=run,
    )
    file_menu.add_separator()
    file_menu.add_command(
        label='Exit',
        command=close,
    )
    help_menu = tk.Menu(menubar)
    help_menu.add_command(
        label='About',
        command=lambda:messagebox.showinfo("About Eimiga Menu", "Eimiga Menu by JakubKwantowy\nv1.0\n\xA9 JakubKwantowy 2022"),
    )
    program_menu = tk.Menu(menubar)
    program_menu.add_command(
        label='Bash',
        command=bash,
    )
    menubar.add_cascade(
        label="File",
        menu=file_menu,
        underline=0
    )
    menubar.add_cascade(
        label="Programs",
        menu=program_menu,
        underline=0
    )
    menubar.add_cascade(
        label="Help",
        menu=help_menu,
        underline=0
    )

    root.config(menu=menubar)

    root.mainloop()
    exit()

if __name__ == "__main__": main()