import os
import cv2
import matplotlib.pyplot as plt

from IPython.display import YouTubeVideo, display, HTML
from base64 import b64encode


source = 'video/race_car.mp4'  # source = 0 for webcam

cap = cv2.VideoCapture(source)

if not cap.isOpened():
    print("Error opening video stream or file")

# Default resolutions of the frame are obtained.
# Convert the resolutions from float to integer.
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# Define the codec and create VideoWriter object.
out_avi = cv2.VideoWriter("video/race_car_out.avi", cv2.VideoWriter_fourcc(*'XVID'), 10, (frame_width, frame_height))
out_mp4 = cv2.VideoWriter("video/race_car_out.mp4", cv2.VideoWriter_fourcc(*'mp4v'), 10, (frame_width, frame_height))

#Read frames and write to file
while cap.isOpened():
    # Capture frame-by-frame
    ret, frame = cap.read()

    if ret:
        # Write the frame to the output files
        out_avi.write(frame)
        out_mp4.write(frame)

    # Break the loop
    else:
        break

# When everything done, release the VideoCapture and VideoWriter objects
cap.release()
out_avi.release()
out_mp4.release()


#___________________________________________________

import subprocess

# Commande d'installation de ffmpeg
command = "sudo apt-get -qq install ffmpeg"

# Exécution de la commande
subprocess.call(command, shell=True)

# Change video encoding of mp4 file from XVID to h264
subprocess.call(f'ffmpeg -y -i "video/race_car_out.mp4" -c:v libx264 "race_car_out_x264.mp4"  -hide_banner -loglevel error', shell=True)

cap = cv2.VideoCapture("race_car_out_x264.mp4")
if not cap.isOpened():
    print("Error opening video stream or file")

while True:
    ret, frame = cap.read()
    if not ret:
        break  # Fin de la vidéo

    cv2.imshow('Video', frame)

    # Appuyez sur la touche 'q' pour quitter la lecture
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()