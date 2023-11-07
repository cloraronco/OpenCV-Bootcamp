import os
import cv2
import matplotlib.pyplot as plt
import numpy as np

from zipfile import ZipFile
from urllib.request import urlretrieve


def p():
	input("Press Enter to continue...")



# Read image as gray scale.
# Read image as unchaged = -1 or cv2.IMREAD_UNCHANGED
# Read image as gray scale = 0 or cv2.IMREAD_GRAYSCALE
# Read image as color scale = 1 or cv2.IMREAD_COLOR  (default flag)

cb_img = cv2.imread("import/checkerboard_18x18.png", 0)

# Print the image data (pixel values), element of a 2D numpy array.
# Each pixel value is 8-bits [0,255]

print(cb_img), p()

# print the size  of image
print("Image size (H, W) is:", cb_img.shape)

# print data-type of image
print("Data type of image is:", cb_img.dtype), p()

# Display image.
plt.imshow(cb_img)
plt.show()

# Set color map to gray scale for proper rendering.
plt.imshow(cb_img, cmap="gray")
plt.show(), p()

#__________________________________________
# ANOTHER EXEMPLE

# Read image as gray scale.
cb_img_fuzzy = cv2.imread("import/checkerboard_fuzzy_18x18.jpg", 0)

# print image
print(cb_img_fuzzy), p()

# Display image.
plt.imshow(cb_img_fuzzy, cmap="gray")
plt.show()

# _________________________________
# WITH COCA-COLA

# Read in image
coke_img = cv2.imread("import/coca-cola-logo.png", 1)

# print the size  of image
print("Image size (H, W, C) is:", coke_img.shape)

# print data-type of image
print("Data type of image is:", coke_img.dtype), p()

plt.imshow(coke_img)
plt.show()

# The color displayed above is different from the actual image.
# This is because matplotlib expects the image in RGB format
# whereas OpenCV stores images in BGR format.
# Thus, for correct display, we need to reverse the channels of the image.

coke_img_channels_reversed = coke_img[:, :, ::-1]
plt.imshow(coke_img_channels_reversed)
plt.show()