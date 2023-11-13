import cv2
import numpy as np
import matplotlib.pyplot as plt


image = cv2.imread("images/Apollo_11_Launch.jpg", cv2.IMREAD_COLOR)

# Draw a rectangle (thickness is a positive integer)
imageRectangle = image.copy()

cv2.rectangle(imageRectangle, (500, 100), (700, 600), (255, 0, 255), thickness=5, lineType=cv2.LINE_8)

# Display the image
plt.imshow(imageRectangle[:, :, ::-1])
plt.savefig("images/draw_rectangle.jpg")
plt.show()