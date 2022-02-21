

# Imports #


from tkinter import *
import tkinter.ttk as ttk
from tkinter import filedialog
from tkinter import messagebox
import tkinter.scrolledtext as scrolledtext
import os


# Functions #


def settings():
    messagebox.showerror("CodeBuddy 4.0", "This feature coming soon.")


def new_file():
    codeText.place(x=35, y=25)
    codeSave.place(x=0, y=25)
    codeRun.place(x=0, y=50)


def save_as():
    messagebox.showerror("CodeBuddy 4.0", "This feature coming soon.")


def save():
    w_file = open("new.py", "w")
    w_file.write(codeText.get("1.0", "end"))
    w_file.close()


def run():
    os.system("new.py")
    print("")
    print("Process ended.")


def restart():
    messagebox.showerror("CodeBuddy 4.0", "This feature coming soon.")


def read_file():
    file = filedialog.askopenfilename()
    opened = open(file, "r")
    print(opened.read())


def open_file():
    messagebox.showerror("CodeBuddy 4.0", "This feature coming soon.")


# GUI #


root = Tk()
root.geometry("800x600")
root.title("CodeBuddy 4.0")

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New File", command=new_file)
filemenu.add_command(label="Open File", command=open_file)
filemenu.add_command(label="Read File", command=read_file)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
filemenu.add_command(label="Restart", command=restart)
menubar.add_cascade(label="File", menu=filemenu)


winmenu = Menu(menubar, tearoff=0)
winmenu.add_command(label="Settings", command=settings)
menubar.add_cascade(label="Window", menu=winmenu)

codeText = scrolledtext.ScrolledText(root, height=35, width=90)

codeSave = ttk.Button(root, text="Save", width=4, command=save)

codeRun = ttk.Button(root, text="Run", width=4, command=run)

root.config(menu=menubar)
root.mainloop()
