import cv2
import numpy as np
import matplotlib.pyplot as plt



img_NZ_bgr = cv2.imread("images/New_Zealand_Boat.jpg", cv2.IMREAD_COLOR)
img_NZ_rgb = img_NZ_bgr[:, :, ::-1]

# Fip images
img_NZ_rgb_flipped_horz = cv2.flip(img_NZ_rgb, 1)
img_NZ_rgb_flipped_vert = cv2.flip(img_NZ_rgb, 0)
img_NZ_rgb_flipped_both = cv2.flip(img_NZ_rgb, -1)

# Show the images
plt.figure(figsize=(18, 5))
plt.subplot(144), plt.imshow(img_NZ_rgb), plt.title("Original"), plt.axis("off")
plt.subplot(141), plt.imshow(img_NZ_rgb_flipped_horz), plt.title("Horizontal Flip"), plt.axis("off")
plt.subplot(142), plt.imshow(img_NZ_rgb_flipped_vert), plt.title("Vertical Flip"), plt.axis("off")
plt.subplot(143), plt.imshow(img_NZ_rgb_flipped_both), plt.title("Both Flipped"), plt.axis("off")
plt.show()