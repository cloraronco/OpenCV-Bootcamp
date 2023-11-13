import cv2
import numpy as np
import matplotlib.pyplot as plt


image = cv2.imread("images/Apollo_11_Launch.jpg", cv2.IMREAD_COLOR)

imageText = image.copy()
text = "Apollo 11 Saturn V Launch, July 16, 1969"
fontScale = 2.3
fontFace = cv2.FONT_HERSHEY_PLAIN
fontColor = (0, 255, 0)
fontThickness = 2

cv2.putText(imageText, text, (200, 700), fontFace, fontScale, fontColor, fontThickness, cv2.LINE_AA)

# Display the image
plt.imshow(imageText[:, :, ::-1])
plt.savefig("images/add_text.jpg")
plt.show()