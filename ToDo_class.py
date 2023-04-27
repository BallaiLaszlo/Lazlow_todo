#!/usr/bin/env python3
from tkinter import *
from Task_info import *

FONT = ("Arial", 20)
SIZE = "600x600"


class to_do_app:
    def __init__(self, master):
        self.master = master
        self.tasks = []
        master.title("To-Do List")
        master.geometry(SIZE)

        self.btn_add = Button(master, text="Add", command=self.add_task, font=FONT)
        self.btn_add.pack()

        self.btn_remove = Button(master, text="Remove", command=self.remove_task, font=FONT)
        self.btn_remove.pack()

        self.btn_info = Button(master, text="Info", command=self.show_task_info, font=FONT)
        self.btn_info.pack()

        self.lst_tasks = Listbox(master, font=FONT)
        self.lst_tasks.pack(pady=10)

    def add_task(self):
        info_window = Toplevel(self.master)
        info_window.title("Add Task")
        info_window.geometry("500x300")

        task_label = Label(info_window, text="Enter task name:", font=FONT)
        task_label.pack(pady=10)

        task_entry = Entry(info_window, font=FONT)
        task_entry.pack(pady=10)

        info_label = Label(info_window, text="Enter task info:", font=FONT)
        info_label.pack(pady=10)

        info_entry = Entry(info_window, font=FONT)
        info_entry.pack(pady=10)

        btn_save = Button(info_window, text="Save", font=FONT,
                          command=lambda: self.save_task(task_entry.get(), info_entry.get(), info_window))
        btn_save.pack(pady=10)

    def save_task(self, task: str, info: str, window=None):
        self.tasks.append({"task": task, "info": info})
        self.lst_tasks.insert(END, task)
        print(f"New task added: {task} - {info}")
        window.destroy()

    def remove_task(self):
        selected_task = self.lst_tasks.curselection()
        self.lst_tasks.delete(selected_task)

    def show_task_info(self):
        selected_task = self.lst_tasks.get(self.lst_tasks.curselection())
        show_task_info(selected_task)
