from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3


class ExitClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1100x500+220+130')
        self.root.title("Inventory Management System")
        self.root.config(bg="white")
        self.root.focus_force()
        
        
if __name__ == "__main__":

    root = Tk()
    obj = ExitClass(root)
    root.mainloop()
