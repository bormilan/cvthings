import cv2
import numpy as np

def simple_edge_detection(image, treshold_1, treshold_2): 
   image = np.uint8(image)
   gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
   edges_detected = cv2.Canny(gray_image , treshold_1, treshold_2) 
   images = [image , edges_detected]
   return images

def main():
    image = cv2.imread('zizi.jpg')
    #plt.imshow(image)
    edges = simple_edge_detection(image, 200, 300)[1]
    cv2.imwrite("edge_zizi.jpg", edges)

main()