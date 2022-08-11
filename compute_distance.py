import cv2 as cv

def find_template(img, template):
    method = eval('cv.TM_CCOEFF')

    res = cv.matchTemplate(img,template,method)
    _, _, _, max_loc = cv.minMaxLoc(res)

    return max_loc

img1 = cv.imread('hatter_calib1.jpg', 0)
img2 = cv.imread('hatter_calib2.jpg', 0)
template = cv.imread('calibration_table.webp',0)
template = cv.resize(template, (500, 500), interpolation = cv.INTER_AREA)

old_koord = find_template(img1, template)
new_koord = find_template(img2, template)

w, h = template.shape[::-1]
result = cv.rectangle(img2,old_koord, (old_koord[0] + w, old_koord[1] + h), (0, 0, 255), 2)

result = cv.rectangle(result,new_koord, (new_koord[0] + w, new_koord[1] + h), (0, 0, 255), 2)
result = cv.line(result, new_koord, old_koord, (0, 0, 255), 2)
print(f"x: {new_koord[0] - old_koord[0]} ")
print(f"y: {new_koord[1] - old_koord[1]} ")

cv.imshow("result", result)
cv.waitKey(0)