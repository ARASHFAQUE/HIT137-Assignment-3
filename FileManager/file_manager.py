import cv2
from tkinter import filedialog

class FileManager:
    def __init__(self): 
        self.history = []
        self.redo_stack = []
        self.file_path = None

    # ---------------- OPEN ----------------
    def open_image(self):
        path = filedialog.askopenfilename(
            filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp")]
        )
        if path:
            self.file_path = path
            img = cv2.imread(path)
            if img is not None:
       
                self.history = [img.copy()]
                self.redo_stack.clear()
                return img
        return None

    # ---------------- SAVE ----------------
    def save(self, image):
        """
        Always ask user where to save the image.
        Behaves like Save As every time.
        """
        return self.save_as(image)

    # ---------------- SAVE AS ----------------
    def save_as(self, image):
        path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[
                ("PNG files", "*.png"),
                ("JPEG files", "*.jpg"),
                ("BMP files", "*.bmp"),
                ("All files", "*.*")
            ]
        )
        if path:
            cv2.imwrite(path, image)
            self.file_path = path
            return path
        return None

    def add_history(self, image):
        self.history.append(image.copy())
        self.redo_stack.clear()

    def undo(self):
        if len(self.history) > 1:
            self.redo_stack.append(self.history.pop())
            return self.history[-1].copy()
        return None

    def redo(self):
        if self.redo_stack:
            img = self.redo_stack.pop()
            self.history.append(img.copy())
            return img.copy()
        return None