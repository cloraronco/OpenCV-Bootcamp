import os
import cv2
import matplotlib.pyplot as plt
import numpy as np

from zipfile import ZipFile
from urllib.request import urlretrieve


download_and_unzip(path_file)

read_image(file_path, format)

matrix(cb_img)

check_attribute(cb_img)


# Display image.
plt.imshow(cb_img)
plt.show()

# Set color map to gray scale for proper rendering.
plt.imshow(cb_img, cmap="gray")
plt.show()
press_enter()

#__________________________________________
# ANOTHER EXEMPLE

# Read image as gray scale.
cb_img_fuzzy = cv2.imread("import/checkerboard_fuzzy_18x18.jpg", 0)

# print image
print(cb_img_fuzzy)
press_enter()

# Display image.
plt.imshow(cb_img_fuzzy, cmap="gray")
plt.show()

_________________________________
# WITH COCA-COLA

# Read in image
coke_img = cv2.imread("import/coca-cola-logo.png", 1)

# print the size  of image
print("Image size (H, W, C) is:", coke_img.shape)

# print data-type of image
print("Data type of image is:", coke_img.dtype)
press_enter()

plt.imshow(coke_img)
plt.show()

# The color displayed above is different from the actual image.
# This is because matplotlib expects the image in RGB format
# whereas OpenCV stores images in BGR format.
# Thus, for correct display, we need to reverse the channels of the image.
reverse_channels(img)