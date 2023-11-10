import os
import cv2
import matplotlib.pyplot as plt

from IPython.display import YouTubeVideo, display, HTML
from base64 import b64encode


source = 'video/race_car.mp4'  # source = 0 for webcam

cap = cv2.VideoCapture(source)

if not cap.isOpened():
    print("Error opening video stream or file")


# Read and display one frame
ret, frame = cap.read()
plt.imshow(frame[..., ::-1])
plt.show()

# Display the video file on jupyter
video = YouTubeVideo("RwxVEjv78LQ", width=700, height=438)
display(video)


# on VScode
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