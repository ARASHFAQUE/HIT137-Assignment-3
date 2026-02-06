# HIT137 Image Editor  
### Desktop Image Processing Application

---

## Overview

The **HIT137 Image Editor** is a desktop-based image processing application developed using  
**Python**, **Tkinter**, and **OpenCV**.

The project demonstrates a strong understanding of **GUI development**, **image processing**,  
**modular software architecture**, and **state management**, while maintaining a clean and intuitive user experience.

This application allows users to open, edit, preview, and save images using a structured control panel and standard desktop interaction patterns.

---

## Project Goals

- Apply image processing techniques using OpenCV  
- Design a responsive and user-friendly GUI  
- Implement reliable undo/redo functionality  
- Follow modular and maintainable software design principles  
- Align with professional desktop application standards  

---

##  Features at a Glance

### Image Processing
- Grayscale conversion  
- Gaussian blur (adjustable intensity)  
- Canny edge detection  
- Brightness adjustment  
- Contrast adjustment  
- Image rotation (90°, 180°, 270°)  
- Image flip (horizontal & vertical)  
- Image resize / scale  

### User Interface
- Sidebar control panel with buttons and sliders  
- Real-time image preview  
- Status bar displaying file name and resolution  

### File Operations
- Open images (JPG, PNG, BMP)  
- Save (overwrite existing file)  
- Save As (choose location, name, and format)  

### Undo / Redo
- Global undo and redo across all features  
- Snapshot-based history tracking  
- Automatic redo stack reset on new actions  

---

## Project Structure

HIT137-Assignment-3/
│
├── main.py
│
├── ImageEditorApp/
│ ├── image_editor_app.py
│ └── init.py
│
├── image_processor.py
├── file_manager.py
│
└── README.md


---

## Architectural Overview

The application follows a **clear separation of concerns**:

| Component | Responsibility |
|--------|----------------|
| **ImageEditorApp** | GUI layout, menus, buttons, sliders, and event handling |
| **ImageProcessor** | All image manipulation operations using OpenCV |
| **FileManager** | File I/O, save logic, and undo/redo state management |
| **main.py** | Application entry point and GUI initialization |

This structure improves readability, scalability, and maintainability.

---

## Running the Application

### Requirements

Ensure Python 3 is installed, then install dependencies:

```bash
pip install opencv-python pillow

▶ Launch

From the project root directory:

python3 main.py

Save Behaviour Explained

Save

Overwrites the currently opened image file.

If no save path exists, the user is prompted automatically.

Save As

Always prompts the user to select:

File name

Save location

Image format

This mirrors standard desktop application behaviour.

Undo & Redo Logic

Every image operation is stored as an immutable snapshot.

Undo restores the immediately previous state.

Redo reapplies the undone operation.

Any new action clears the redo stack.

This guarantees predictable and consistent editing behaviour.

Authors

Sydney Group 1 — HIT137 (Software Now)

Md Ashfaqur Rahman — S397791

Md Mubtasim Fuad Jenok — S399056

Md Abdullah All Mamun Udoy — S397684

Mohona Islam — S398918

License & Usage

This project is developed exclusively for academic purposes as part of the HIT137 coursework.

Not intended for commercial use

Redistribution requires academic approval

All rights reserved to the authors

Final Remarks

This project reflects:

Clean and modular design

Thoughtful user experience decisions

Robust state and file management

Practical application of image processing concepts

It serves both as an academic submission and a foundational demonstration of professional Python desktop application development.