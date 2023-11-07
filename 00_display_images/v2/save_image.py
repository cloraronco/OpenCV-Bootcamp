import cv2
import matplotlib.pyplot as plt
import numpy as np


def save_image(file_path, img):
	cv.imwrite(file_path, img)