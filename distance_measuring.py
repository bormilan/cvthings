import cv2
import numpy as np

img = cv2.imread("seeger1.jpg")

print(img.shape)

first = ((400, 320),(500, 420))
second = ((580, 320), (680, 420))


cv2.rectangle(img, (first[0][0], first[0][1]), (first[1][0], first[1][1]), (0, 0, 255), 3)
cv2.rectangle(img, (second[0][0], second[0][1]), (second[1][0], second[1][1]), (0, 0, 255), 3)
o1 = int((first[0][0] + first[1][0]) / 2), int((first[0][1] + first[1][1]) / 2)
o2 = int((second[0][0] + second[1][0]) / 2), int((second[0][1] + second[1][1]) / 2)

cv2.circle(img, o1, 10, (0,0,255), -1)
cv2.circle(img, o2, 10, (0,0,255), -1)

cv2.line(img,(o1[0], o1[1]), (o2[0], o2[1]), (0, 0, 255), 5)
print(f"A két középpont távolsága: {np.linalg.norm(np.array(o2) - np.array(o1))}")


cv2.imshow("gorilla", img)



cv2.waitKey(0) 
cv2.destroyAllWindows() 