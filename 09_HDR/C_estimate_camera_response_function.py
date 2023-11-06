import cv2
import numpy as np
import matplotlib.pyplot as plt


def estimate_camera_response_function(images, times):
    # Find Camera Response Function (CRF)
    calibrateDebevec = cv2.createCalibrateDebevec()
    responseDebevec = calibrateDebevec.process(images, times)

    # Plot CRF
    x = np.arange(256, dtype=np.uint8)
    y = np.squeeze(responseDebevec)

    ax = plt.figure(figsize=(30, 10))
    plt.title("Debevec Inverse Camera Response Function", fontsize=24)
    plt.xlabel("Measured Pixel Value", fontsize=22)
    plt.ylabel("Calibrated Intensity", fontsize=22)
    plt.xlim([0, 260])
    plt.grid()
    plt.plot(x, y[:, 0], "r", x, y[:, 1], "g", x, y[:, 2], "b")
    plt.show()

    return images, times, responseDebevec