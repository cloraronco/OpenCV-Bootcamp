import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def pause():
	input("Press Enter to continue...")



# Read image as gray scale.
cb_img = cv.imread("images/checkerboard_18x18.png", 0)

# Set color map to gray scale for proper rendering.
plt.imshow(cb_img, cmap="gray")
plt.show()
print(cb_img)

# print the first pixel of the first black box
print("matrix[0,0]: ",cb_img[0, 0])
# print the first white pixel to the right of the first black box
print("matrix[0,6]: ",cb_img[0, 6])
pause()

# ________PAUSE________

cb_img_copy = cb_img.copy()
cb_img_copy[2, 2] = 200
cb_img_copy[2, 3] = 200
cb_img_copy[3, 2] = 200
cb_img_copy[3, 3] = 200

# Same as above
# cb_img_copy[2:3,2:3] = 200

plt.imshow(cb_img_copy, cmap="gray")
plt.show()
print(cb_img_copy)