import numpy as np
import cv2 as cv
img = cv.imread('new_item_kit1.jpeg')
# gray= cv.cvtColor(img,cv.COLOR_BGR2GRAY)
sift = cv.SIFT_create()
kp = sift.detect(img,None)
img=cv.drawKeypoints(img,kp,img)
cv.imshow('sift_keypoints.jpg',img)
cv.waitKey(0)