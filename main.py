from tkinter import *
from Task_info import *
from ToDo_class import *


def main():
    root = Tk()
    todo_app = to_do_app(root)
    root.mainloop()


if __name__ == '__main__':
    main()
