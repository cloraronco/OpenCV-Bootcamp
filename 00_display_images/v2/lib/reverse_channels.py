import cv2
import matplotlib.pyplot as plt
import numpy as np

# To display with Matplotlib, an image that has been read using OpenCV (cv2).

# Matplotlib expects the image in RGB format
# whereas OpenCV stores images in BGR format.
# Thus, for correct display, we need to reverse the channels of the image.

def reverse_channels(img):
	img_channels_reversed = img[:, :, ::-1]
	return img_channels_reversed