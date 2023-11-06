import cv2
import numpy as np
import matplotlib.pyplot as plt
import A_capture_multi_explosures


def align_images():
    # Read images and exposure times
    images, times = A_capture_multi_explosures.readImagesAndTimes()

    # Align Images
    alignMTB = cv2.createAlignMTB()
    alignMTB.process(images, images)

    return images, times