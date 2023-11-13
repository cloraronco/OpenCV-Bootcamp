import cv2
import numpy as np
import matplotlib.pyplot as plt


img_rec = cv2.imread("images/rectangle.jpg", cv2.IMREAD_GRAYSCALE)

img_cir = cv2.imread("images/circle.jpg", cv2.IMREAD_GRAYSCALE)

plt.figure(figsize=[18, 5])
plt.subplot(121), plt.title("Rectangle"), plt.imshow(img_rec, cmap="gray")
plt.subplot(122), plt.title("Circle"), plt.imshow(img_cir, cmap="gray")
plt.savefig("images/bitwise_figure.png")
plt.show()
print(img_rec.shape)


# Mask= The `mask` parameter is a binary image that determines which pixels of the output image (`result` in your case) will be computed based on the input images (`img_rec` and `img_cir` in your case).
# In this case, `mask=None` Pixels for which the mask value is non-zero will be considered in the computation.

# Bitwise AND Operator
plt.figure(figsize=[18, 5])
result = cv2.bitwise_and(img_rec, img_cir, mask=None)
plt.subplot(131)
plt.imshow(result, cmap="gray")
plt.title("Bitwise AND")

# Bitwise OR Operator
result = cv2.bitwise_or(img_rec, img_cir, mask=None)
plt.subplot(132)
plt.imshow(result, cmap="gray")
plt.title("Bitwise OR")

# Bitwise XOR Operator
result = cv2.bitwise_xor(img_rec, img_cir, mask=None)
plt.subplot(133)
plt.imshow(result, cmap="gray")
plt.title("Bitwise XOR")

plt.savefig("images/bitwise_operator.png")
plt.show()