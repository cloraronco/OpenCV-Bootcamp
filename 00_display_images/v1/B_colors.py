import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


# Splitting and Merging Color Channels

img_NZ_bgr = cv.imread("import/New_Zealand_Lake.jpg", cv.IMREAD_COLOR)

# Split the image into the B,G,R components
b, g, r = cv.split(img_NZ_bgr)

plt.imshow(b)
plt.show()

# Show the channels
fig, axes = plt.subplots(1, 4, figsize=(18, 5))

axes[0].imshow(r, cmap="gray")
axes[0].set_title("Red Channel")
axes[0].axis("off")

axes[1].imshow(g, cmap="gray")
axes[1].set_title("Green Channel")
axes[1].axis("off")

axes[2].imshow(b, cmap="gray")
axes[2].set_title("Blue Channel")
axes[2].axis("off")

# Merge the individual channels into a BGR image
imgMerged = cv.merge((b, g, r))

# Show the merged output
axes[3].imshow(imgMerged[:, :, ::-1])
axes[3].set_title("Merged Output")
axes[3].axis("off")

# Ajustement automatique de la disposition pour éviter le chevauchement
plt.tight_layout()
plt.savefig("images/split_merge_color.jpg")
plt.show()


# OpenCV stores color channels in a differnet order than most other applications (BGR vs RGB).
img_NZ_rgb = cv.cvtColor(img_NZ_bgr, cv.COLOR_BGR2RGB)
plt.imshow(img_NZ_rgb)
plt.show()


# Changing to HSV color space
img_hsv = cv.cvtColor(img_NZ_bgr, cv.COLOR_BGR2HSV)

# Split the image into the B,G,R components
h,s,v = cv.split(img_hsv)

# Show the channels
plt.figure(figsize=[16,4])
# h for color
plt.subplot(141);plt.imshow(h, cmap="gray");plt.title("H Channel")
# s for saturation/ intensity
plt.subplot(142);plt.imshow(s, cmap="gray");plt.title("S Channel")
# v for value
plt.subplot(143);plt.imshow(v, cmap="gray");plt.title("V Channel")
plt.subplot(144);plt.imshow(img_NZ_rgb);   plt.title("Original");plt.show()


#____________________________________________________________
# MODIFYING INDIVIDUAL CHANNEL

h_new = h + 10
img_NZ_merged = cv.merge((h_new, s, v))
img_NZ_rgb = cv.cvtColor(img_NZ_merged, cv.COLOR_HSV2RGB)

# Show the channels
plt.figure(figsize=[16,4])
plt.subplot(141);plt.imshow(h, cmap="gray");plt.title("H Channel")
plt.subplot(142);plt.imshow(s, cmap="gray");plt.title("S Channel")
plt.subplot(143);plt.imshow(v, cmap="gray");plt.title("V Channel")
plt.subplot(144);plt.imshow(img_NZ_rgb);   plt.title("Original"); plt.show()

#____________________________________________________________
# SAVING IMAGES

# save image
cv.imwrite("import/New_Zealand_Lake_SAVED.png", img_NZ_bgr)

#read image
lake_img = cv.imread("import/New_Zealand_Lake_SAVED.png")

# Use OpenCV imshow(), display until any key is pressed
window3 = cv.namedWindow("w3")
cv.imshow(window3, lake_img)
cv.waitKey(0)
cv.destroyWindow(window3)

# plt.imshow("image/New_Zealand_Lake_SAVED.png") 
# plt.show()

# read the image as Color
img_NZ_bgr = cv.imread("import/New_Zealand_Lake_SAVED.png", cv.IMREAD_COLOR)
print("img_NZ_bgr shape (H, W, C) is:", img_NZ_bgr.shape)

# read the image as Grayscaled
img_NZ_gry = cv.imread("import/New_Zealand_Lake_SAVED.png", cv.IMREAD_GRAYSCALE)
print("img_NZ_gry shape (H, W) is:", img_NZ_gry.shape)