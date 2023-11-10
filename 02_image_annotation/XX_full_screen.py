import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


#___________________FULL SCREEN DISPLAY___________________

import tkinter as tk
from PIL import Image, ImageTk

# Load your image using OpenCV
image = cv.imread("images/Apollo_11_Launch.jpg")

# Create a Tkinter window
root = tk.Tk()
root.title("OpenCV Image")

# Convert the OpenCV image to a format that Tkinter can display
image_rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)
image_pil = Image.fromarray(image_rgb)
photo = ImageTk.PhotoImage(image=image_pil)

# Create a Tkinter label to display the image
label = tk.Label(root, image=photo)
label.pack()

# Start the Tkinter main loop
root.mainloop()