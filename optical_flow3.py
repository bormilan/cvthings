import numpy as np
import cv2 as cv
import argparse
parser = argparse.ArgumentParser(description='This sample demonstrates Lucas-Kanade Optical Flow calculation. \
                                              The example file can be downloaded from: \
                                              https://www.bogotobogo.com/python/OpenCV_Python/images/mean_shift_tracking/slow_traffic_small.mp4')
parser.add_argument('image1', type=str, help='path to image file')
parser.add_argument('image2', type=str, help='path to image file')
args = parser.parse_args()

sift = cv.SIFT_create(1000, 10, 0.04, 10, 1.6)

# Parameters for lucas kanade optical flow
lk_params = dict( winSize  = (15, 15),
                  maxLevel = 2,
                  criteria = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 0.03))

# Create some random colors
color = np.random.randint(0, 255, (78992, 3))
# Take first frame and find corners in it
old_frame = cv.imread(args.image1)
old_gray = cv.cvtColor(old_frame, cv.COLOR_BGR2GRAY)
kp = sift.detect(old_gray,None)
# Create a mask image for drawing purposes
mask = np.zeros_like(old_frame)

frame = cv.imread(args.image2)
# print(f"{kp[0].pt[0]}, {kp[0].pt[0]}")
p0 = np.array([np.array([np.array([np.float32(p.pt[0]), np.float32(p.pt[1])])]) for p in kp])

# print(type(p0[0][0][0]))
# print(p0)

frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
# calculate optical flow
p1, st, err = cv.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)

# Select good points
if p1 is not None:
    good_new = p1[st==1]
    good_old = p0[st==1]
# draw the tracks
distances = good_new - good_old
print(len(good_new))
# print(f"{good_new} - {good_old} = {distances}")
for i, (new, old) in enumerate(zip(good_new, good_old)):
    a, b = new.ravel()
    c, d = old.ravel()
    mask = cv.line(mask, (int(a), int(b)), (int(c), int(d)), color[i].tolist(), 2)
    frame = cv.circle(frame, (int(a), int(b)), 5, color[i].tolist(), -1)
img = cv.add(frame, mask)
cv.imshow('frame1', old_frame)
cv.imshow('frame2', img)

cv.waitKey(0)
cv.destroyAllWindows()