import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


# Splitting and Merging Color Channels

img_NZ_bgr = cv.imread("image/New_Zealand_Lake.jpg", cv.IMREAD_COLOR)

def split_and_merge(img_bgr):
	# Split the image into the B,G,R components
	b, g, r = cv.split(img_NZ_bgr)

	# Show the channels
	plt.figure(figsize=[18, 5])

	plt.subplot(141);plt.imshow(r, cmap="gray");plt.title("Red Channel")
	plt.subplot(142);plt.imshow(g, cmap="gray");plt.title("Green Channel")
	plt.subplot(143);plt.imshow(b, cmap="gray");plt.title("Blue Channel")

	# Merge the individual channels into a BGR image
	imgMerged = cv.merge((b, g, r))
	# Show the merged output
	plt.subplot(144)
	plt.imshow(imgMerged[:, :, ::-1])
	plt.title("Merged Output")
	plt.show()


def bgr_to_rgb(img_bgr):
	# OpenCV stores color channels in a differnet order than most other applications (BGR vs RGB).
	img_rgb = cv.cvtColor(img_bgr, cv.COLOR_BGR2RGB)
	plt.imshow(img_rgb)
	plt.show()


#____________________________________________________________
# CHANGING TO HSV COLOR SPACE

img_hsv = cv.cvtColor(img_NZ_bgr, cv.COLOR_BGR2HSV)

# Split the image into the B,G,R components
h,s,v = cv.split(img_hsv)

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
img_NZ_merged = cv.merge((h_new, s, v))
img_NZ_rgb = cv.cvtColor(img_NZ_merged, cv.COLOR_HSV2RGB)

# Show the channels
plt.figure(figsize=[16,4])
plt.subplot(141);plt.imshow(h, cmap="gray");plt.title("H Channel")
plt.subplot(142);plt.imshow(s, cmap="gray");plt.title("S Channel")
plt.subplot(143);plt.imshow(v, cmap="gray");plt.title("V Channel")
plt.subplot(144);plt.imshow(img_NZ_rgb);   plt.title("Original"); plt.show()

#____________________________________________________________
# SAVING IMAGES

def save_image(file_path, img):
	# save image
	cv.imwrite("image/New_Zealand_Lake_SAVED.png", img_NZ_bgr)

#read image
lake_img = cv.imread("image/New_Zealand_Lake_SAVED.png")

# Use OpenCV imshow(), display until any key is pressed
window3 = cv.namedWindow("w3")
cv.imshow(window3, lake_img)
cv.waitKey(0)
cv.destroyWindow(window3)

# plt.imshow("image/New_Zealand_Lake_SAVED.png") 
# plt.show()

# read the image as Color
img_NZ_bgr = cv.imread("image/New_Zealand_Lake_SAVED.png", cv.IMREAD_COLOR)
print("img_NZ_bgr shape (H, W, C) is:", img_NZ_bgr.shape)

# read the image as Grayscaled
img_NZ_gry = cv.imread("image/New_Zealand_Lake_SAVED.png", cv.IMREAD_GRAYSCALE)
print("img_NZ_gry shape (H, W) is:", img_NZ_gry.shape)