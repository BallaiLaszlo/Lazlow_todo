#!/usr/bin/env python3
from tkinter import *

FONT = ("Arial", 16)


def show_task_info(task: str):
    info_window = Toplevel()
    info_window.title(f"Info about {task}")
    info_window.geometry("650x200")

    lbl_info = Label(info_window, text=f"info about {task}: {task.entry.get()}")
