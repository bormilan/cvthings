import cv2
import os
from autocontrast import automatic_brightness_and_contrast

path = "/Users/bormilan/Documents/plm_kepek_detect/test_raw"
path_to = "/Users/bormilan/Documents/plm_kepek_detect/test5"

# for img in os.listdir(path):
#     if img != ".DS_Store":
#         pic = cv2.imread(os.path.join(path,img))       
#         cropped_img = pic[ 410:510, 380:480 ]
#         pic = automatic_brightness_and_contrast(pic, 10)

#         cv2.imwrite(os.path.join(path_to,img), cropped_img)

path_ = "/Users/bormilan/Documents/plm_kepek_detect/test4/test.jpg"

pic = cv2.imread(path_)       
cropped_img = pic[ 210:510, 380:480 ]
pic = automatic_brightness_and_contrast(pic, 10)

cv2.imwrite("cropped.jpg",cropped_img)