from __future__ import print_function
import cv2 as cv
import argparse

def detectAndDisplay(frame):
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    frame_gray = cv.equalizeHist(frame_gray)
    gorilla = cv.imread("viki2.jpeg")
    # gorilla = gorilla[: , 200:500]
    gorilla = gorilla[:400 , 300:600]

    #-- Detect faces
    faces = face_cascade.detectMultiScale(frame_gray)
    for (x,y,w,h) in faces:
        center = (x + w//2, y + h//2)

        resized_gorilla = gorilla
        width = int(gorilla.shape[1] * (w * 0.3) / 100)
        height = int(gorilla.shape[0] * (h * 0.3) / 100)
        resized_gorilla = cv.resize(gorilla, (width, height), interpolation = cv.INTER_AREA)

        if x + resized_gorilla.shape[1] <= frame.shape[1] and y + resized_gorilla.shape[0] <= frame.shape[0]:
            frame[y : y + resized_gorilla.shape[0], x : x + resized_gorilla.shape[1]] = resized_gorilla
        # frame = cv.ellipse(frame, center, (w//2, h//2), 0, 0, 360, (255, 0, 255), 4)
        faceROI = frame_gray[y:y+h,x:x+w]
        #-- In each face, detect eyes
        # eyes = eyes_cascade.detectMultiScale(faceROI)
        # for (x2,y2,w2,h2) in eyes:
        #     eye_center = (x + x2 + w2//2, y + y2 + h2//2)
        #     radius = int(round((w2 + h2)*0.25))
        #     frame = cv.circle(frame, eye_center, radius, (255, 0, 0 ), 4)

    frame = image = cv.flip(frame, 1)
    cv.imshow('Capture - Face detection', frame)

parser = argparse.ArgumentParser(description='Code for Cascade Classifier tutorial.')
parser.add_argument('--face_cascade', help='Path to face cascade.', default='/Users/bormilan/miniforge3/pkgs/libopencv-4.5.5-py39h8339426_3/share/opencv4/haarcascades/haarcascade_frontalface_alt.xml')
parser.add_argument('--eyes_cascade', help='Path to eyes cascade.', default='/Users/bormilan/miniforge3/pkgs/libopencv-4.5.5-py39h8339426_3/share/opencv4/haarcascades/haarcascade_eye_tree_eyeglasses.xml')
parser.add_argument('--camera', help='Camera divide number.', type=int, default=0)

args = parser.parse_args()

face_cascade_name = args.face_cascade
eyes_cascade_name = args.eyes_cascade
face_cascade = cv.CascadeClassifier()
eyes_cascade = cv.CascadeClassifier()

#-- 1. Load the cascades
if not face_cascade.load(cv.samples.findFile(face_cascade_name)):
    print('--(!)Error loading face cascade')
    exit(0)
if not eyes_cascade.load(cv.samples.findFile(eyes_cascade_name)):
    print('--(!)Error loading eyes cascade')
    exit(0)
camera_device = args.camera

#-- 2. Read the video stream
cap = cv.VideoCapture(camera_device)

if not cap.isOpened:
    print('--(!)Error opening video capture')
    exit(0)
while True:
    ret, frame = cap.read()
    if frame is None:
        print('--(!) No captured frame -- Break!')
        break
    detectAndDisplay(frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        cv.destroyAllWindows()
        break