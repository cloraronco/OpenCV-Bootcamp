import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


img_bgr = cv.imread("images/New_Zealand_Coast.jpg", cv.IMREAD_COLOR)
img_rgb = cv.cvtColor(img_bgr, cv.COLOR_BGR2RGB)

#  --> img_rgb = img_bgr[:, :, ::-1]

plt.imshow(img_rgb)
plt.show()


matrix = np.ones(img_rgb.shape, dtype="uint8") * 50

img_rgb_brighter = cv.add(img_rgb, matrix)
img_rgb_darker   = cv.subtract(img_rgb, matrix)


# Show the images
plt.figure(figsize=[18, 5])
plt.subplot(131), plt.imshow(img_rgb_darker),  plt.title("Darker")
plt.subplot(132), plt.imshow(img_rgb),         plt.title("Original")
plt.subplot(133), plt.imshow(img_rgb_brighter),plt.title("Brighter")
plt.show()