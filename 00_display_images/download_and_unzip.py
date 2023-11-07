import os
import cv2
import matplotlib.pyplot as plt
import numpy as np

from zipfile import ZipFile
from urllib.request import urlretrieve


def download_and_unzip(path_file):
	def download_and_unzip1(url, save_path):
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

	URL = r"https://www.dropbox.com/s/qhhlqcica1nvtaw/opencv_bootcamp_assets_NB1.zip?dl=1"

	asset_zip_path = os.path.join(os.getcwd(), path_file)

	## Download if assest ZIP does not exists.
	if not os.path.exists(asset_zip_path):
		download_and_unzip1(URL, asset_zip_path)