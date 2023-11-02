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

# # Read in image
# coke_img = cv2.imread("image/coca-cola-logo.png", 1)

# # print the size  of image
# print("Image size (H, W, C) is:", coke_img.shape)

# # print data-type of image
# print("Data type of image is:", coke_img.dtype), p()

# plt.imshow(coke_img)
# plt.show()

# # The color displayed above is different from the actual image.
# # This is because matplotlib expects the image in RGB format
# # whereas OpenCV stores images in BGR format.
# # Thus, for correct display, we need to reverse the channels of the image.
# # We will discuss about the channels in the sections below.

# coke_img_channels_reversed = coke_img[:, :, ::-1]
# plt.imshow(coke_img_channels_reversed)
# plt.show(), p()


#____________________________________________________________
#____________________________________________________________
# Splitting and Merging Color Channels

# # cv2.split() Divides a multi-channel array into several single-channel arrays.
# # cv2.merge() Merges several arrays to make a single multi-channel array.
# # 	All the input matrices must have the same size.

# # Split the image into the B,G,R components
img_NZ_bgr = cv2.imread("image/New_Zealand_Lake.jpg", cv2.IMREAD_COLOR)
# b, g, r = cv2.split(img_NZ_bgr)

# # Show the channels
# plt.figure(figsize=[20, 5])

# plt.subplot(141);plt.imshow(r, cmap="gray");plt.title("Red Channel")
# plt.subplot(142);plt.imshow(g, cmap="gray");plt.title("Green Channel")
# plt.subplot(143);plt.imshow(b, cmap="gray");plt.title("Blue Channel")

# # Merge the individual channels into a BGR image
# imgMerged = cv2.merge((b, g, r))
# # Show the merged output
# plt.subplot(144)
# plt.imshow(imgMerged[:, :, ::-1])
# plt.title("Merged Output")
# plt.show(), p()

#______________________________________________
# CHANGING FROM BGR TO RGB

# OpenCV stores color channels in a differnet order than most other applications (BGR vs RGB).
img_NZ_rgb = cv2.cvtColor(img_NZ_bgr, cv2.COLOR_BGR2RGB)
plt.imshow(img_NZ_rgb)
plt.show()


#____________________________________________________________
# CHANGING TO HSV COLOR SPACE

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
plt.subplot(144);plt.imshow(img_NZ_rgb);   plt.title("Original");plt.show()


#____________________________________________________________
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

#____________________________________________________________
# SAVING IMAGES

# save image
cv2.imwrite("image/New_Zealand_Lake_SAVED.png", img_NZ_bgr)

#read image
lake_img = cv2.imread("image/New_Zealand_Lake_SAVED.png")

# Use OpenCV imshow(), display until any key is pressed
window3 = cv2.namedWindow("w3")
cv2.imshow(window3, lake_img)
cv2.waitKey(0)
cv2.destroyWindow(window3)

# plt.imshow("image/New_Zealand_Lake_SAVED.png") 
# plt.show()

# read the image as Color
img_NZ_bgr = cv2.imread("image/New_Zealand_Lake_SAVED.png", cv2.IMREAD_COLOR)
print("img_NZ_bgr shape (H, W, C) is:", img_NZ_bgr.shape)

# read the image as Grayscaled
img_NZ_gry = cv2.imread("image/New_Zealand_Lake_SAVED.png", cv2.IMREAD_GRAYSCALE)
print("img_NZ_gry shape (H, W) is:", img_NZ_gry.shape)