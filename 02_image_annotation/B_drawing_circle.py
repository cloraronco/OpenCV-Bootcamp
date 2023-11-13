import cv2
import numpy as np
import matplotlib.pyplot as plt


image = cv2.imread("images/Apollo_11_Launch.jpg", cv2.IMREAD_COLOR)

# Draw a circle
imageCircle = image.copy()

cv2.circle(imageCircle, (900, 500), 100, (0, 0, 255), thickness=5, lineType=cv2.LINE_AA)

# Display the image
cv2.imshow("imageCircle", imageCircle)

plt.imshow(imageCircle[:, :, ::-1])
plt.savefig("images/draw_circle.jpg")
plt.show()
