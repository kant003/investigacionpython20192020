# Basado en https://towardsdatascience.com/face-detection-in-2-minutes-using-opencv-python-90f89d7c0f81
import numpy as np
import argparse
import cv2
import imutils
import time
from collections import deque
from imutils.video import VideoStream

ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help="path to the (optional) video file")
ap.add_argument("-b", "--buffer", type=int, default=64, help="max buffer size")

args = vars(ap.parse_args())

# Open webcam if video file is not supplied
if not args.get('video', False):
    vs = VideoStream(ssrc=0).start()

else:
    vs = cv2.VideoCapture(args['video'])

time.sleep(2.0)

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


while True:
    frame = vs.read()
    frame = frame[1] if args.get('video', False) else frame
    if frame is None:
        break

    frame = imutils.resize(frame, width=600)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # Draw rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    # Display the output
    cv2.imshow('img', frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

if not args.get("video", False):
    vs.stop()
else:
    vs.release()
    
cv2.destroyAllWindows()
