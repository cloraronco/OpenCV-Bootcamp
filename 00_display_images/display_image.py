import os
import cv2
import matplotlib.pyplot as plt
import numpy as np

from zipfile import ZipFile
from urllib.request import urlretrieve

from IPython.display import Image

# %matplotlib inline


def p():
	input("Press Enter to continue...")

def download_and_unzip(url, save_path):
	print(f"Downloading and extracting assests....", end="")

	# Downloading zip file using urllib package.
	urlretrieve(url, save_path)

	try:
		# Extracting zip file using the zipfile package.
		with ZipFile(save_path) as z:
			# Extract ZIP file contents in the same directory.
			z.extractall(os.path.split(save_path)[0])

		print("Done")

	except Exception as e:
		print("\nInvalid file.", e)

URL = r"https://www.dropbox.com/s/qhhlqcica1nvtaw/opencv_bootcamp_assets_NB1.zip?dl=1"

asset_zip_path = os.path.join(os.getcwd(), "import/opencv_bootcamp_assets_NB1.zip")

## Download if assest ZIP does not exists.
if not os.path.exists(asset_zip_path):
	download_and_unzip(URL, asset_zip_path)


#_________________________________________________________________________#


# # Display 18x18 pixel image.
# Image(filename="image/checkerboard_18x18.png")

# # Display 84x84 pixel image.
# Image(filename="image/checkerboard_84x84.jpg")

# # Read image as gray scale.
# cb_img = cv2.imread("image/checkerboard_18x18.png", 0)

# # Print the image data (pixel values), element of a 2D numpy array.
# # Each pixel value is 8-bits [0,255]

# print(cb_img), p()

# # print the size  of image
# print("Image size (H, W) is:", cb_img.shape)

# # print data-type of image
# print("Data type of image is:", cb_img.dtype), p()

# # Display image.
# plt.imshow(cb_img)
# plt.show()

# # Set color map to gray scale for proper rendering.
# plt.imshow(cb_img, cmap="gray")
# plt.show(), p()

# #__________________________________________
# # ANOTHER EXEMPLE

# # Read image as gray scale.
# cb_img_fuzzy = cv2.imread("image/checkerboard_fuzzy_18x18.jpg", 0)

# # print image
# print(cb_img_fuzzy), p()

# # Display image.
# plt.imshow(cb_img_fuzzy, cmap="gray")
# plt.show()

#_________________________________
# WITH COCA-COLA

# Read in image
coke_img = cv2.imread("image/coca-cola-logo.png", 1)

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
# We will discuss about the channels in the sections below.

coke_img_channels_reversed = coke_img[:, :, ::-1]
plt.imshow(coke_img_channels_reversed)
plt.show()


#____________________________________________________________
#____________________________________________________________
# Splitting and Merging Color Channels