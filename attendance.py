# import re
import re
from sys import path
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
import mysql.connector
import cv2
import numpy as np
from tkinter import messagebox
from time import strftime
from datetime import datetime
import csv
from tkinter import filedialog

import os
import mysql.connector
from tkinter import *
from tkinter import ttk, filedialog, messagebox
import share

class Attendance:
    
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Attendance Panel")
        # Other initialization code...

        # Open folder corresponding to username
        username = "your_username_here"  # Replace "your_username_here" with actual username
        folder_path = os.path.join(r"C:\Users\rajpa\Documents\Python_Test_Projects\attendance",share.value)
        if os.path.exists(folder_path):
            os.startfile(folder_path)
        else:
            messagebox.showerror("Error", "Folder not found for the specified username.")

if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
