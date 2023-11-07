import os
import cv2
import matplotlib.pyplot as plt
import numpy as np
import lib

from zipfile import ZipFile
from urllib.request import urlretrieve


# Download and unzip
lib.download_and_unzip("import/opencv_bootcamp_assets_NB1.zip")


# 1
# Read image as gray scale.
# Read image as unchaged = -1 or cv2.IMREAD_UNCHANGED
# Read image as gray scale = 0 or cv2.IMREAD_GRAYSCALE
# Read image as color scale = 1 or cv2.IMREAD_COLOR  (default flag)

img = cv2.imread("import/checkerboard_18x18.png", 0)

# Print size and data-type of image
lib.check_attribute(img)

# Display image
plt.imshow(img)
plt.show()


# 2
# Read in image
coke_img = cv2.imread("import/coca-cola-logo.png", 1)
lib.display_plt(coke_img)

# The color displayed above is different from the actual image.
# This is because matplotlib expects the image in RGB format
# whereas OpenCV stores images in BGR format.
# Thus, for correct display, we need to reverse the channels of the image.

coke_img_channels_reversed = lib.reverse_channels(coke_img)
lib.display_plt(coke_img_channels_reversed)


# 3
# Splitting and Merging Color Channels
img_NZ_bgr = cv2.imread("import/New_Zealand_Lake.jpg", cv2.IMREAD_COLOR)
lib.split_merge_display(img_NZ_bgr)

# OpenCV stores color channels in a differnet order than most other applications (BGR vs RGB).
img_NZ_rgb = lib.bgr_to_rgb(img_NZ_bgr)

# Changing to HSV color space
img_hsv = cv2.cvtColor(img_NZ_bgr, cv2.COLOR_BGR2HSV)

# Split the image into the B,G,R components
h,s,v = cv2.split(img_hsv)

# Show the channels
plt.figure(figsize=[16,4])
# h for color
plt.subplot(141);plt.imshow(h, cmap="gray");plt.title("H Channel")
# s for saturation/ intensity
plt.subplot(142);plt.imshow(s, cmap="gray");plt.title("S Channel")
# v for value
plt.subplot(143);plt.imshow(v, cmap="gray");plt.title("V Channel")
plt.subplot(144);plt.imshow(img_NZ_rgb);plt.title("Original");plt.show()

# MODIFYING INDIVIDUAL CHANNEL

h_new = h + 10
img_NZ_merged = cv2.merge((h_new, s, v))
img_NZ_rgb = cv2.cvtColor(img_NZ_merged, cv2.COLOR_HSV2RGB)

# Show the channels
plt.figure(figsize=[16,4])
plt.subplot(141);plt.imshow(h, cmap="gray");plt.title("H Channel")
plt.subplot(142);plt.imshow(s, cmap="gray");plt.title("S Channel")
plt.subplot(143);plt.imshow(v, cmap="gray");plt.title("V Channel")
plt.subplot(144);plt.imshow(img_NZ_rgb);   plt.title("Original"); plt.show()

# save image
new_file = "import/New_Zealand_Lake_SAVED.png"
cv2.imwrite(new_file, img_NZ_bgr)
# image saved

# read image
lib.read_display("import/New_Zealand_Lake_SAVED.png")

# a
img_NZ_bgr = cv2.imread("import/New_Zealand_Lake_SAVED.png", cv2.IMREAD_COLOR)
img_NZ_gry = cv2.imread("import/New_Zealand_Lake_SAVED.png", cv2.IMREAD_GRAYSCALE)
