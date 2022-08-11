import cv2

img = cv2.imread("zizi.jpg")
# img = img[500:2000 , 500:2000]
resized = cv2.resize(img, (300,400), interpolation = cv2.INTER_AREA)
print(resized.shape)
cv2.imshow("",resized)

cv2.imwrite("resized_zizi.jpeg", resized)

cv2.waitKey(0)
cv2.destroyAllWindows()