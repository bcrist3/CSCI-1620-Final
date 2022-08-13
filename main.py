from gui import *
from tkinter import ttk


def main():
    window = Tk()
    # Sets the window name
    window.title('Calculator')
    # Sets the window geometry
    window.geometry('500x600')
    # Makes the window unable to be resizabled
    window.resizable(False, False)
    # Creates a notebook
    notebook = ttk.Notebook(window)
    widgets = GUI(window, notebook)
    window.mainloop()


if __name__ == '__main__':
    main()
