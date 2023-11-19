import os
import cv2
import math
import glob
import numpy as np
import matplotlib.pyplot as plt




def init():
	images_folder = "images"
	if not os.path.exists(images_folder):
		os.makedirs(images_folder)

	# Ouvrir la vidéo
	cap = cv2.VideoCapture("quais.mp4")

	# Vérifier si la vidéo est ouverte correctement
	if not cap.isOpened():
		print("Erreur lors de l'ouverture de la vidéo.")
		exit()

	# Variables pour le compteur d'images et le compteur de frames
	count_images = 0
	count_frames = 0
	frame_interval = 10  # Afficher et enregistrer chaque 10e frame
	subset_size = 5 # Créer un dossier "subset" toutes les 5 sauvegardes de frame

	count_file = 0
	subset = 0

	while True:
		# Lire une frame de la vidéo
		ret, frame = cap.read()
		if not ret:
			break  # Fin de la vidéo

		# Incrémenter le compteur de frames
		count_frames += 1

		# Créer un dossier "subset" toutes les 5 sauvegardes de frame
		if count_file % subset_size == 0:
			subset = f"subset{int(count_file / subset_size)}"
			subset_path = os.path.join("images", subset)
			os.makedirs(subset_path, exist_ok=True)

		# Afficher et enregistrer chaque 10e frame
		if count_frames % frame_interval == 0:
			# Sauvegarder la frame dans un fichier image
			file_name = os.path.join(subset_path, f"frame{count_images}.jpg")  
			cv2.imwrite(file_name, frame)
			count_file += 1

			# Incrémenter le compteur d'images
			count_images += 1

		# Appuyez sur la touche 'q' pour quitter la lecture
		if cv2.waitKey(25) & 0xFF == ord('q'):
			break

	# Libérer la capture
	cap.release()

	# Fermer toutes les fenêtres
	cv2.destroyAllWindows()

	print("count_images: ", count_images)
	print("count_frames: ", count_frames)
	print("count_file: ", count_file)

	return count_file