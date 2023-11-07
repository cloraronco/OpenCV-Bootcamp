import cv2
import matplotlib.pyplot as plt
import numpy as np

# Use OpenCV imshow(), display until any key is pressed
def read_until_keypress(img):
    window = cv.namedWindow("w")
    cv.imshow(window, lake_img)
    cv.waitKey(0)
    cv.destroyWindow(window)