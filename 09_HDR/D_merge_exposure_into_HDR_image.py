import cv2
import numpy as np
import matplotlib.pyplot as plt


def merge_images(images, times, responseDebevec):
    # Merge images into an HDR linear image
    mergeDebevec = cv2.createMergeDebevec()
    hdrDebevec = mergeDebevec.process(images, times, responseDebevec)

    return hdrDebevec