import cv2
import numpy as np
import matplotlib.pyplot as plt


def readImagesAndTimes():
    # List of file names
    filenames = ["import/img_0.033.jpg", "import/img_0.25.jpg", "import/img_2.5.jpg", "import/img_15.jpg"]

    # List of exposure times
    times = np.array([1 / 30.0, 0.25, 2.5, 15.0], dtype=np.float32)

    # Read images
    images = []
    for filename in filenames:
        im = cv2.imread(filename)
        im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
        images.append(im)

    return images, times