import cv2

img = cv2.imread("/Users/bormilan/Downloads/20220722_104119_cucu.jpeg")

image = cv2.copyMakeBorder(img, 500, 500, 200, 200, cv2.BORDER_DEFAULT)

cv2.imwrite("with_padding.jpeg", image)
print(image.shape)
