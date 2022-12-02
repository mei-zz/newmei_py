"""
找一个自己喜欢的照片或者海报，通过Sobel或者Canny算子，
对照片或海报进行处理，调整参数使处理后的效果尽可能凸显主题。
"""
import cv2 as cv
import numpy as np

init_img=cv.imread("2.jpg",cv.IMREAD_GRAYSCALE)

res_img = cv.Canny(init_img, 100, 120)
# 参数：设置两个阈值，分别为上界和下届：在这两个阈值之间的内容会别保存下来，其余部分别删去
# 两个参数越小，保留的细节就越多。
# 第二个参数越小意味着判断图像中的边缘阈值也越小，更多的内容会被判断成边缘信息
res = np.hstack((init_img, res_img))
cv.namedWindow("res",cv.WINDOW_NORMAL)
cv.imshow('res',res)
cv.waitKey(0)
cv.destroyAllWindows()
