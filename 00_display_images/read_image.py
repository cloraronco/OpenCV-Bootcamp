import cv2
import matplotlib.pyplot as plt
import numpy as np


# Read image as unchaged = -1 or cv2.IMREAD_COLOR
# Read image as gray scale = 0 or cv2.IMREAD_GRAYSCALE
# Read image as color scale = 1 or cv2.IMREAD_COLOR  (default flag)

def read_image(file_path, format):
	cb_img = cv2.imread(file_path, format)
	return cb_img