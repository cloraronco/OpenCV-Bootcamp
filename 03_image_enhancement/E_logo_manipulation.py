import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


# ______Read foreground image______

img_bgr = cv.imread("images/coca-cola-logo.png")
img_rgb = cv.cvtColor(img_bgr, cv.COLOR_BGR2RGB)

print(img_rgb.shape)

logo_w = img_rgb.shape[0]
logo_h = img_rgb.shape[1]


# ______Read background image______

# Read in image of color cheackerboad background
img_background_bgr = cv.imread("images/checkerboard_color.png")
img_background_rgb = cv.cvtColor(img_background_bgr, cv.COLOR_BGR2RGB)

# Set desired width (logo_w) and maintain image aspect ratio
aspect_ratio = logo_w / img_background_rgb.shape[1]
dim = (logo_w, int(img_background_rgb.shape[0] * aspect_ratio))


# REMIND : interpolation
# interpolation=cv.INTER_AREA: This argument specifies the interpolation algorithm used to resize the image.
# In this example, cv.INTER_AREA is used, indicating the use of Area-based interpolation, which is commonly employed for downsampling.


# Resize background image to sae size as logo image
img_background_rgb = cv.resize(img_background_rgb, dim, interpolation=cv.INTER_AREA)

print(img_background_rgb.shape)

plt.figure(figsize=[18, 5])
plt.subplot(121), plt.axis("off"), plt.title("Logo"), plt.imshow(img_rgb)
plt.subplot(122), plt.axis("off"), plt.title("Backgroung"), plt.imshow(img_background_rgb)
plt.savefig("images/logo_transformation1.png")


#______Create mask for original image______

img_gray = cv.cvtColor(img_rgb, cv.COLOR_RGB2GRAY)

# Apply global thresholding to creat a binary mask of the logo
retval, img_mask = cv.threshold(img_gray, 127, 255, cv.THRESH_BINARY)

print(img_mask.shape)



#______Invert the mask______

# Create an inverse mask
img_mask_inv = cv.bitwise_not(img_mask)


plt.figure(figsize=[18, 5])
plt.subplot(121), plt.axis("off"), plt.title("Apply global thresholding to creat a binary mask of the logo"), plt.imshow(img_mask, cmap="gray")
plt.subplot(122), plt.axis("off"), plt.title("Create an inverse mask"), plt.imshow(img_mask_inv, cmap="gray")
plt.savefig("images/logo_transformation2.png")

plt.show()

#______Apply the mask on background______

# Create colorful background "behind" the logo lettering
img_background = cv.bitwise_and(img_background_rgb, img_background_rgb, mask=img_mask)


#______Isolate foreground from image______

# Isolate foreground (red from original image) using the inverse mask
img_foreground = cv.bitwise_and(img_rgb, img_rgb, mask=img_mask_inv)



#______Result: Merge Foreground and Background______

# Add the two previous results obtain the final result
result = cv.add(img_background, img_foreground)
cv.imwrite("images/logo_final.png", result[:, :, ::-1])



# Affichage sur deux lignes


plt.figure(figsize=[18, 5])

plt.subplot(131), plt.axis("off"), plt.title("Apply the mask on background", fontsize=14), plt.imshow(img_background)
plt.subplot(132), plt.axis("off"), plt.title("Create an inverse mask", fontsize=14), plt.imshow(img_foreground)
plt.subplot(133), plt.axis("off"), plt.title("Result: Merge Foreground and Background", fontsize=14), plt.imshow(result)

plt.savefig("images/logo_transformation3.png")

plt.show()

