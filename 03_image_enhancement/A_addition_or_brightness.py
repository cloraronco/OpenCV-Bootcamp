import cv2
import numpy as np
import matplotlib.pyplot as plt


img_bgr = cv2.imread("images/New_Zealand_Coast.jpg", cv2.IMREAD_COLOR)
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

#  --> img_rgb = img_bgr[:, :, ::-1]

plt.imshow(img_rgb)
plt.show()


matrix = np.ones(img_rgb.shape, dtype="uint8") * 50

img_rgb_brighter = cv2.add(img_rgb, matrix)
img_rgb_darker   = cv2.subtract(img_rgb, matrix)


# Show the images
plt.figure(figsize=[18, 5])
plt.subplot(131), plt.axis("off"), plt.imshow(img_rgb_darker),  plt.title("Darker")
plt.subplot(132), plt.axis("off"), plt.imshow(img_rgb),         plt.title("Original")
plt.subplot(133), plt.axis("off"), plt.imshow(img_rgb_brighter),plt.title("Brighter")
plt.savefig("images/brightness.jpg")
plt.show()
