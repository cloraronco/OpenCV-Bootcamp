import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

from IPython.display import Image

#___________________ENTIRE SCREEN DISPLAY___________________

import screeninfo

# Get the screen size
screen = screeninfo.get_monitors()[0]
screen_width, screen_height = screen.width, screen.height

# Load your image
image = cv.imread("images/Apollo_11_Launch.jpg")

# Create a window that spans the entire screen
cv.namedWindow('Biggest Window', cv.WND_PROP_FULLSCREEN)
cv.setWindowProperty('Biggest Window', cv.WND_PROP_FULLSCREEN, cv.WINDOW_FULLSCREEN)

# Display the image in the window
cv.imshow('Biggest Window', image)

# Wait for a key press and then close the window
cv.waitKey(0)
cv.destroyAllWindows()