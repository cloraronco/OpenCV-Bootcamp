import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


image = cv.imread("images/Apollo_11_Launch.jpg", cv.IMREAD_COLOR)

imageText = image.copy()
text = "Apollo 11 Saturn V Launch, July 16, 1969"
fontScale = 2.3
fontFace = cv.FONT_HERSHEY_PLAIN
fontColor = (0, 255, 0)
fontThickness = 2

cv.putText(imageText, text, (200, 700), fontFace, fontScale, fontColor, fontThickness, cv.LINE_AA)

# Display the image
plt.imshow(imageText[:, :, ::-1])
plt.show()