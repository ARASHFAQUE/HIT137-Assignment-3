import cv2
import numpy as np
import copy

class ImageProcessor:
    def __init__(self):
        self._image = None

        # ---------------- Feature-specific history ----------------
        self.history_grayscale = []
        self.history_blur = []
        self.history_edge = []
        self.history_rotate = []
        self.history_flip = []
        self.history_resize = []
        self.history_brightness_contrast = []

    # ---------------- GET/SET ----------------
    def set_image(self, image):
        self._image = image

    def get_image(self):
        return self._image

    # ---------------- FEATURE UNDO ----------------
    def undo_grayscale(self):
        if self.history_grayscale:
            self._image = self.history_grayscale.pop()
        return self._image

    def undo_blur(self):
        if self.history_blur:
            self._image = self.history_blur.pop()
        return self._image

    def undo_edge(self):
        if self.history_edge:
            self._image = self.history_edge.pop()
        return self._image

    def undo_rotate(self):
        if self.history_rotate:
            self._image = self.history_rotate.pop()
        return self._image

    def undo_flip(self):
        if self.history_flip:
            self._image = self.history_flip.pop()
        return self._image

    def undo_resize(self):
        if self.history_resize:
            self._image = self.history_resize.pop()
        return self._image

    def undo_brightness_contrast(self):
        if self.history_brightness_contrast:
            self._image = self.history_brightness_contrast.pop()
        return self._image

    # ---------------- ACTIONS ----------------
    def grayscale(self):
        if self._image is None:
            return None
        self.history_grayscale.append(copy.deepcopy(self._image))
        gray = cv2.cvtColor(self._image, cv2.COLOR_BGR2GRAY)
        self._image = gray
        return gray

    def blur(self, ksize):
        if self._image is None:
            return None
        self.history_blur.append(copy.deepcopy(self._image))
        if ksize % 2 == 0:
            ksize += 1
        blurred = cv2.GaussianBlur(self._image, (ksize, ksize), 0)
        self._image = blurred
        return blurred
