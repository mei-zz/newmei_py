
import cv2 as cv
import numpy as np

init_img=cv.imread("2.jpg",cv.IMREAD_GRAYSCALE)

res_img = cv.Canny(init_img, 100, 120)
res = np.hstack((init_img, res_img))
cv.namedWindow("res",cv.WINDOW_NORMAL)
cv.imshow('res',res)
cv.waitKey(0)
cv.destroyAllWindows()
