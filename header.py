import os
import cv2
import matplotlib.pyplot as plt
import numpy as np

from zipfile import ZipFile
from urllib.request import urlretrieve

from IPython.display import Image

# %matplotlib inline

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

## Display 18x18 pixel image.
# Image(filename="checkerboard_18x18.png")

## Display 84x84 pixel image.
# Image(filename="checkerboard_84x84.jpg")

## Read image as gray scale.
# cb_img = cv2.imread("checkerboard_18x18.png", 0)

## Print the image data (pixel values), element of a 2D numpy array.
## Each pixel value is 8-bits [0,255]

# print(cb_img)

## print the size  of image
# print("Image size (H, W) is:", cb_img.shape)

## print data-type of image
# print("Data type of image is:", cb_img.dtype)

## Display image.
# plt.imshow(cb_img)
# plt.show()

## Set color map to gray scale for proper rendering.
# plt.imshow(cb_img, cmap="gray")
# plt.show()

## ANOTHER EXEMPLE
## Read image as gray scale.
cb_img_fuzzy = cv2.imread("checkerboard_fuzzy_18x18.jpg", 0)

## print image
print(cb_img_fuzzy)

## Display image.
plt.imshow(cb_img_fuzzy, cmap="gray")
plt.show()