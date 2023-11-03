import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


# Read in an image
image = cv.imread("images/Apollo_11_Launch.jpg", cv.IMREAD_COLOR)

# Display the original image
plt.imshow(image[:, :, ::-1])
plt.show()


imageLine = image.copy()

# The line starts from (200,100) and ends at (400,100)
# The color of the line is YELLOW (Recall that OpenCV uses BGR format)
# Thickness of line is 5px
# Linetype is cv2.LINE_AA

cv.line(imageLine, (200, 100), (400, 100), (0, 255, 255), thickness=5, lineType=cv.LINE_AA)

# Display the image
plt.imshow(imageLine[:,:,::-1])
plt.show()