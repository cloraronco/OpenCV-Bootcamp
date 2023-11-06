import cv2
import numpy as np
import matplotlib.pyplot as plt


def tonnemapping(hdrDebevec):
    # Tonemap using Drago's method to obtain 24-bit color image
    print("Tonemaping using Drago's method ... ")
    tonemapDrago = cv2.createTonemapDrago(1.0, 0.7)
    ldrDrago = tonemapDrago.process(hdrDebevec)
    ldrDrago = 3 * ldrDrago

    plt.title("Tonemap using Drago's method", fontsize=24)
    plt.figure(figsize=(20, 10));plt.imshow(np.clip(ldrDrago, 0, 1));plt.axis("off")

    cv2.imwrite("ldr-Drago.jpg", ldrDrago * 255)
    print("saved ldr-Drago.jpg")

    # Tonemap using Reinhard's method to obtain 24-bit color image
    print("Tonemaping using Reinhard's method ... ")
    tonemapReinhard = cv2.createTonemapReinhard(1.5, 0, 0, 0)
    ldrReinhard = tonemapReinhard.process(hdrDebevec)

    plt.title("Tonemap using Reinhard's method", fontsize=24)
    plt.figure(figsize=(20, 10));plt.imshow(np.clip(ldrReinhard, 0, 1));plt.axis("off")

    cv2.imwrite("ldr-Reinhard.jpg", ldrReinhard * 255)
    print("saved ldr-Reinhard.jpg")

    # Tonemap using Mantiuk's method to obtain 24-bit color image
    print("Tonemaping using Mantiuk's method ... ")
    tonemapMantiuk = cv2.createTonemapMantiuk(2.2, 0.85, 1.2)
    ldrMantiuk = tonemapMantiuk.process(hdrDebevec)
    ldrMantiuk = 3 * ldrMantiuk

    plt.title("Tonemap using Mantiuk's method", fontsize=24)
    plt.figure(figsize=(20, 10));plt.imshow(np.clip(ldrMantiuk, 0, 1));plt.axis("off")

    cv2.imwrite("ldr-Mantiuk.jpg", ldrMantiuk * 255)
    print("saved ldr-Mantiuk.jpg")