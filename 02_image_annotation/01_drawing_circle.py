import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


image = cv.imread("images/Apollo_11_Launch.jpg", cv.IMREAD_COLOR)

# Draw a circle
imageCircle = image.copy()

cv.circle(imageCircle, (900, 500), 100, (0, 0, 255), thickness=5, lineType=cv.LINE_AA)

# Display the image
cv.imshow("imageCircle", imageCircle)

plt.imshow(imageCircle[:, :, ::-1])
plt.show()
