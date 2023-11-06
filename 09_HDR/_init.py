import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

from zipfile import ZipFile
from urllib.request import urlretrieve

import A_capture_multi_explosures
import B_align_images
import C_estimate_camera_response_function
import D_merge_exposure_into_HDR_image
import E_tonnemapping

def download_and_unzip(url, save_path):
    print(f"Downloading and extracting assests....", end="")

    # Downloading zip file using urllib package.
    urlretrieve(url, save_path)

    try:
        # Extracting zip file using the zipfile package.
        with ZipFile(save_path) as z:
            # Extract ZIP file contents in the same directory.
            z.extractall(os.path.split(save_path)[0])

        print("Done")

    except Exception as e:
        print("\nInvalid file.", e)


URL = r"https://www.dropbox.com/s/qa1hsyxt66pvj02/opencv_bootcamp_assets_NB10.zip?dl=1"

asset_zip_path = os.path.join(os.getcwd(), "import/opencv_bootcamp_assets_NB10.zip")

# Download if assest ZIP does not exists.
if not os.path.exists(asset_zip_path):
    download_and_unzip(URL, asset_zip_path)



images, times = B_align_images.align_images()
images, times, responseDebevec = C_estimate_camera_response_function.estimate_camera_response_function(images, times)
hdrDebevec = D_merge_exposure_into_HDR_image.merge_images(images, times, responseDebevec)
E_tonnemapping.tonnemapping(hdrDebevec)