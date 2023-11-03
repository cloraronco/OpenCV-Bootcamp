import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


img_rec = cv.imread("images/rectangle.jpg", cv.IMREAD_GRAYSCALE)

img_cir = cv.imread("images/circle.jpg", cv.IMREAD_GRAYSCALE)

plt.figure(figsize=[18, 5])
plt.subplot(121);plt.imshow(img_rec, cmap="gray")
plt.subplot(122);plt.imshow(img_cir, cmap="gray")
plt.show()
print(img_rec.shape)


# Bitwise AND Operator
result = cv.bitwise_and(img_rec, img_cir, mask=None)
plt.imshow(result, cmap="gray")
print("Bitwise AND")
plt.show()

# Bitwise OR Operator
result = cv.bitwise_or(img_rec, img_cir, mask=None)
plt.imshow(result, cmap="gray")
print("Bitwise OR")
plt.show()

# Bitwise XOR Operator
result = cv.bitwise_xor(img_rec, img_cir, mask=None)
plt.imshow(result, cmap="gray")
print("Bitwise XOR")
plt.show()