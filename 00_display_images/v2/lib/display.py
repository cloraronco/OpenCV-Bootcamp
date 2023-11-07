import cv2
import matplotlib.pyplot as plt
import numpy as np

# Use OpenCV imshow()
def display_cv(img):
    cv2.imshow(window, lake_img)

# Use Matplotlib imshow(), show()
def display_plt(img):
    plt.imshow(img)
    plt.show()

# Use OpenCV imshow(), display until any key is pressed
def display_until_keypress(img):
    window = cv2.namedWindow("w")
    cv2.imshow(window, lake_img)
    cv2.waitKey(0)
    cv2.destroyWindow(window)

# Read and display
def read_display(img):
    new_img = cv2.imread(img)
    display_plt(new_img)

