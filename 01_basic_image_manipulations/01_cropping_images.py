import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

from IPython.display import Image

def pause():
	input("Press Enter to continue...")



img_NZ_bgr = cv.imread("images/New_Zealand_Boat.jpg", cv.IMREAD_COLOR)
img_NZ_rgb = img_NZ_bgr[:, :, ::-1]

plt.imshow(img_NZ_rgb)
plt.show()
pause()


# ________Press Enter to continue...________


# Crop out the middle region of the image
cropped_region = img_NZ_rgb[200:400, 300:600]

cv.imwrite("images/cropped_region.png", img_NZ_bgr[200:400, 300:600])

plt.imshow(cropped_region)
plt.show()