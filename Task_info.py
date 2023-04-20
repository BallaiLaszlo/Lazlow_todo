#!/usr/bin/env python3
from tkinter import *
FONT = ("Arial", 16)

def show_task_info(task:str):
    info_window=Toplevel()
    info_window.title(f"Info about {task}")
    info_window.geometry("650x200")

    lbl_info=Label(info_window,text=f"info about {task}: {task.entry.get()}")

def add_info(task:str):
    info_window=Toplevel()
    info_window.title(f"Give info to {task} ")
    info_window.geometry("650x200")

    lbl = Label(info_window, text=f"Enter info about {task}", font=FONT)
    lbl.pack(pady=10)

    entry = Entry(info_window, font=FONT)
    entry.pack(pady=10)
