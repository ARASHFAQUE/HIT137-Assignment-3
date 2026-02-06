import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import cv2
import os



class ImageEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sydney Group-1 Image Editor Assignment-3")
        self.root.geometry("1200x750")
        self.create_menu()
        self.create_ui()

    # ---------------- MENU ----------------
    def create_menu(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Open", command=self.open_image)
        file_menu.add_command(label="Save", command=self.save_image)
        file_menu.add_command(label="Save As", command=self.save_as)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)

        edit_menu = tk.Menu(menubar, tearoff=0)
        edit_menu.add_command(label="Undo", command=self.undo)
        edit_menu.add_command(label="Redo", command=self.redo)

        menubar.add_cascade(label="File", menu=file_menu)
        menubar.add_cascade(label="Edit", menu=edit_menu)