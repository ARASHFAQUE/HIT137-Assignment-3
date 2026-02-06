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
     # ---------------- UI ----------------
    def create_ui(self):
        main_frame = tk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # ---- Control Panel ----
        control_panel = tk.Frame(main_frame, width=250, relief=tk.RIDGE, bd=2)
        control_panel.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)

        tk.Label(control_panel, text="Control Panel", font=("Arial", 12, "bold")).pack(pady=5)

        # Open / Save
        tk.Button(control_panel, text="Open Image", command=self.open_image).pack(fill=tk.X, padx=10, pady=2)
        tk.Button(control_panel, text="Save Image", command=self.save_image).pack(fill=tk.X, padx=10, pady=2)

        # ----------------- Grayscale -----------------
        tk.Button(control_panel, text="Grayscale", command=self.apply_grayscale).pack(fill=tk.X, padx=10, pady=2)
        tk.Button(control_panel, text="Undo Grayscale", command=self.undo_grayscale).pack(fill=tk.X, padx=10, pady=2)

        # ----------------- Blur -----------------
        tk.Label(control_panel, text="Blur Intensity").pack()
        self.blur_slider = tk.Scale(control_panel, from_=1, to=25, orient=tk.HORIZONTAL)
        self.blur_slider.set(9)
        self.blur_slider.pack(fill=tk.X, padx=10)
        tk.Button(control_panel, text="Apply Blur", command=self.apply_blur).pack(fill=tk.X, padx=10, pady=2)
        tk.Button(control_panel, text="Undo Blur", command=self.undo_blur).pack(fill=tk.X, padx=10, pady=2)

        # ----------------- Edge Detection -----------------
        tk.Button(control_panel, text="Edge Detection", command=self.apply_edges).pack(fill=tk.X, padx=10, pady=2)
        tk.Button(control_panel, text="Undo Edge", command=self.undo_edge).pack(fill=tk.X, padx=10, pady=2)

        # ----------------- Brightness / Contrast -----------------
        tk.Label(control_panel, text="Brightness").pack()
        self.brightness_slider = tk.Scale(control_panel, from_=-100, to=100, orient=tk.HORIZONTAL,
                                          command=self.adjust_brightness)
        self.brightness_slider.pack(fill=tk.X, padx=10)

        tk.Label(control_panel, text="Contrast").pack()
        self.contrast_slider = tk.Scale(control_panel, from_=10, to=300, orient=tk.HORIZONTAL,
                                        command=self.adjust_contrast)
        self.contrast_slider.set(100)
        self.contrast_slider.pack(fill=tk.X, padx=10)

        tk.Button(control_panel, text="Undo Brightness/Contrast", command=self.undo_brightness_contrast).pack(fill=tk.X, padx=10, pady=2)

        # ----------------- Rotate -----------------
        tk.Label(control_panel, text="Rotate").pack(pady=5)
        tk.Button(control_panel, text="90°", command=lambda: self.rotate_image(90)).pack(fill=tk.X, padx=10)
        tk.Button(control_panel, text="180°", command=lambda: self.rotate_image(180)).pack(fill=tk.X, padx=10)
        tk.Button(control_panel, text="270°", command=lambda: self.rotate_image(270)).pack(fill=tk.X, padx=10)
        tk.Button(control_panel, text="Undo Rotate", command=self.undo_rotate).pack(fill=tk.X, padx=10, pady=2)

        # ----------------- Flip -----------------
        tk.Label(control_panel, text="Flip").pack(pady=5)
        tk.Button(control_panel, text="Horizontal", command=lambda: self.flip_image(1)).pack(fill=tk.X, padx=10)
        tk.Button(control_panel, text="Vertical", command=lambda: self.flip_image(0)).pack(fill=tk.X, padx=10)
        tk.Button(control_panel, text="Undo Flip", command=self.undo_flip).pack(fill=tk.X, padx=10, pady=2)

        # ----------------- Resize -----------------
        tk.Label(control_panel, text="Resize (%)").pack()
        self.resize_slider = tk.Scale(control_panel, from_=10, to=200, orient=tk.HORIZONTAL)
        self.resize_slider.set(100)
        self.resize_slider.pack(fill=tk.X, padx=10)
        tk.Button(control_panel, text="Apply Resize", command=self.resize_image).pack(fill=tk.X, padx=10, pady=5)
        tk.Button(control_panel, text="Undo Resize", command=self.undo_resize).pack(fill=tk.X, padx=10, pady=2)

        # ---- Image Display ----
        self.image_label = tk.Label(main_frame)
        self.image_label.pack(expand=True)

        self.status = tk.Label(self.root, text="No image loaded", relief=tk.SUNKEN, anchor="w")
        self.status.pack(side=tk.BOTTOM, fill=tk.X)

        
     # ---------------- DISPLAY ----------------
    def display_image(self, image):
        if image is None:
            return

        if len(image.shape) == 2:
            image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        pil = Image.fromarray(rgb)
        pil.thumbnail((900, 650))

        self.tk_img = ImageTk.PhotoImage(pil)
        self.image_label.config(image=self.tk_img)

        name = os.path.basename(self.file_manager.file_path or "")
        h, w = image.shape[:2]
        self.status.config(text=f"{name} | {w} x {h}")

 # ---------------- FILE ----------------
    def open_image(self):
        img = self.file_manager.open_image()
        if img is not None:
            self.processor.set_image(img)
            self.display_image(img)

    def save_image(self):
        img = self.processor.get_image()
        if img is not None:
            path = self.file_manager.save(img)  # This will always ask
        if path:
            messagebox.showinfo("Saved", f"Image saved successfully:\n{path}")

    def save_as(self):
        img = self.processor.get_image()
        if img is not None:
            self.file_manager.save_as(img)

    def update_image(self, img):
        if img is not None:
            self.processor.set_image(img)
            self.file_manager.add_history(img)
            self.display_image(img)

    # ---------------- ACTIONS ----------------
    def apply_grayscale(self):
        self.update_image(self.processor.grayscale())

    def apply_blur(self):
        k = self.blur_slider.get()
        if k % 2 == 0:
            k += 1
        self.update_image(self.processor.blur(k))

    def apply_edges(self):
        self.update_image(self.processor.edge_detection())

    def adjust_brightness(self, value):
        img = self.processor.adjust_brightness_contrast(int(value), None)
        self.display_image(img)

    def adjust_contrast(self, value):
        img = self.processor.adjust_brightness_contrast(None, int(value) / 100)
        self.display_image(img)

    def rotate_image(self, angle):
        self.update_image(self.processor.rotate(angle))

    def flip_image(self, mode):
        self.update_image(self.processor.flip(mode))

    def resize_image(self):
        scale = self.resize_slider.get() / 100
        self.update_image(self.processor.resize(scale))