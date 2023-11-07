import cv2
import matplotlib.pyplot as plt
import numpy as np


def check_attribute(cb_img):
	# print the size  of image
	print("Image size (H, W) is:", cb_img.shape)

	# print data-type of image
	print("Data type of image is:", cb_img.dtype)