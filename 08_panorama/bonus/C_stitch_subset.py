import os
import cv2
import math
import glob
import numpy as np
import matplotlib.pyplot as plt

# def stitch_subset(count_file):

subset_size = 5 # Créer un dossier "subset" toutes les 5 sauvegardes de frame
subset = 0


images_folder = "images2"
if not os.path.exists(images_folder):
    os.makedirs(images_folder)

count_file = 581 * 2

count_subset = int(count_file / 10)
i = 0
count_subset = count_subset / 5
print(count_subset)

while i < count_subset:
    # Read Images
    imagefiles = glob.glob(f"images1/subset{i}/{os.sep}*")
    imagefiles.sort()

    # Créer un dossier "subset" toutes les 5 sauvegardes de frame
    if i % subset_size == 0:
        subset = f"subset{int(i / subset_size)}"
        subset_path = os.path.join("images2", subset)
        os.makedirs(subset_path, exist_ok=True)


    images = []
    for filename in imagefiles:
        img = cv2.imread(filename)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        images.append(img)

    num_images = len(images)

    print(num_images)


    # Stitch Images
    stitcher = cv2.Stitcher_create()
    # stitcher.setWaveCorrection(True)
    status, result = stitcher.stitch(images)

    if status ==0 :
        file_name = os.path.join(subset_path, f"pano{i}.png")
        cv2.imwrite(file_name, cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
    
    i += 1
    # plt.show()
