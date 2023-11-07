import cv2
import matplotlib.pyplot as plt
import numpy as np


# Splitting and Merging Color Channels

# cv.split() Divides a multi-channel array into several single-channel arrays.
# cv.merge() Merges several arrays to make a single multi-channel array.
# 	All the input matrices must have the same size.

def split_merge_display(img_bgr):
	# Split the image into the B,G,R components
	b, g, r = cv.split(img_bgr)

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