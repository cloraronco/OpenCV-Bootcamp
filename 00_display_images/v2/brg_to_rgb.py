import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


def bgr_to_rgb(img_bgr):
	# OpenCV stores color channels in a differnet order than most other applications (BGR vs RGB).
	img_rgb = cv.cvtColor(img_bgr, cv.COLOR_BGR2RGB)
	plt.imshow(img_rgb)
	plt.show()

