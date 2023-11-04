import os
import cv2 as cv
import matplotlib.pyplot as plt

from IPython.display import YouTubeVideo, display, HTML
from base64 import b64encode


source = 'video/race_car.mp4'  # source = 0 for webcam

cap = cv.VideoCapture(source)

if not cap.isOpened():
    print("Error opening video stream or file")

# Default resolutions of the frame are obtained.
# Convert the resolutions from float to integer.
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# Define the codec and create VideoWriter object.
out_avi = cv.VideoWriter("video/race_car_out.avi", cv.VideoWriter_fourcc(*'XVID'), 10, (frame_width, frame_height))
out_mp4 = cv.VideoWriter("video/race_car_out.mp4", cv.VideoWriter_fourcc(*'mp4v'), 10, (frame_width, frame_height))

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
