import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# from IPython.display import Image


image = cv.imread("images/Apollo_11_Launch.jpg", cv.IMREAD_COLOR)


# Draw a rectangle (thickness is a positive integer)
imageRectangle = image.copy()

cv.rectangle(imageRectangle, (500, 100), (700, 600), (255, 0, 255), thickness=5, lineType=cv.LINE_8)

# Display the image
plt.imshow(imageRectangle[:, :, ::-1])
plt.show()