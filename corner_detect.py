import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('csaladi-haz.jpeg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray,25,0.01,10)
corners = np.int0(corners)
print(len(corners))

for i in corners:
    x,y = i.ravel()
    cv2.circle(img,(x,y),10,255,-1)

plt.imshow(img),plt.show()