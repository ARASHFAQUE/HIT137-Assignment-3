import tkinter as tk

def main():
    # Create the main Tkinter window
    root = tk.Tk()

    # Initialize the Image Editor App with the root window
    # and our imageEditorApp class will keep the methods
    app = ImageEditorApp(root)

    # Start the Tkinter main loop
    root.mainloop()

if __name__ == "__main__":
    main()
