import cv2
import numpy as np
import matplotlib.pyplot as plt


img_read = cv2.imread("images/building-windows.jpg", cv2.IMREAD_GRAYSCALE)
retval, img_thresh = cv2.threshold(img_read, 100, 255, cv2.THRESH_BINARY)

# Show the images
plt.figure(figsize=[18, 5])

plt.subplot(121), plt.axis("off"), plt.imshow(img_read, cmap="gray"), plt.title("Original")
plt.subplot(122), plt.axis("off"), plt.imshow(img_thresh, cmap="gray"), plt.title("Thresholded")
plt.savefig("images/threshold.jpg")
plt.show()

print(img_thresh.shape)



# APPLICATION: sheet music reader

# Read the original image
img_read = cv2.imread("images/Piano_Sheet_Music.png", cv2.IMREAD_GRAYSCALE)

# Perform global thresholding
retval, img_thresh_gbl_1 = cv2.threshold(img_read, 50, 255, cv2.THRESH_BINARY)

# Perform global thresholding
retval, img_thresh_gbl_2 = cv2.threshold(img_read, 130, 255, cv2.THRESH_BINARY)

# Perform adaptive thresholding
img_thresh_adp = cv2.adaptiveThreshold(img_read, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 7)

# Show the images
plt.figure(figsize=[18,15])
plt.subplot(221), plt.axis("off"), plt.imshow(img_read,        cmap="gray"), plt.title("Original")
plt.subplot(222), plt.axis("off"), plt.imshow(img_thresh_gbl_1,cmap="gray"), plt.title("Thresholded (global: 50)")
plt.subplot(223), plt.axis("off"), plt.imshow(img_thresh_gbl_2,cmap="gray"), plt.title("Thresholded (global: 130)")
plt.subplot(224), plt.axis("off"), plt.imshow(img_thresh_adp,  cmap="gray"), plt.title("Thresholded (adaptive)")
plt.savefig("images/threshold_perform.jpg")
plt.show()