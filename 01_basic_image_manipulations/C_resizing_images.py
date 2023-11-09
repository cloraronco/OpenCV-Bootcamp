import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

from IPython.display import Image

def pause():
	input("Press Enter to continue...")

cropped_region_bgr = cv.imread("images/cropped_region.png", cv.IMREAD_COLOR)
cropped_region = cropped_region_bgr[:, :, ::-1]


# Method 1: Specifying scaling factor using fx and fy
resized_cropped_region_2x = cv.resize(cropped_region, None, fx=2, fy=2)
plt.imshow(resized_cropped_region_2x)
plt.show()


# Method 2: Specifying exact size of the output image
desired_width = 100
desired_height = 200
dim = (desired_width, desired_height)

# Resize background image to sae size as logo image
resized_cropped_region = cv.resize(cropped_region, dsize=dim, interpolation=cv.INTER_AREA)
plt.imshow(resized_cropped_region)
plt.show()
pause()


#______________Press Enter to continue..._______________


# Resize while maintaining aspect ratio
desired_width = 100
aspect_ratio = desired_width / cropped_region.shape[1]
desired_height = int(cropped_region.shape[0] * aspect_ratio)
dim = (desired_width, desired_height)

# Resize image
resized_cropped_region = cv.resize(cropped_region, dsize=dim, interpolation=cv.INTER_AREA)
plt.imshow(resized_cropped_region)
plt.show()
pause()


#______________Press Enter to continue..._______________



# Swap channel order
resized_cropped_region_2x = resized_cropped_region_2x[:, :, ::-1]

# Save resized image to disk
cv.imwrite("images/resized_cropped_region_2x.png", resized_cropped_region_2x)

# Display the cropped and resized image
resized_cropped_region_bgr = cv.imread("images/resized_cropped_region_2x.png", cv.IMREAD_COLOR)
resized_cropped_region_rgb = resized_cropped_region_bgr[:, :, ::-1]

plt.imshow(resized_cropped_region_rgb)
plt.show()
