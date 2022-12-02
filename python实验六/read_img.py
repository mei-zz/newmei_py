"""
利用opencv读取电脑上的一张图片，
打印出他的尺寸和数据类型，并用matplotlib将图片绘制出来；
"""
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread("2.jpg")
# cv.namedWindow("img1",cv.WINDOW_NORMAL)
# cv.imshow("img1", img)
# cv.waitKey(0)
print(img.shape)  # 打印图片大小
plt.imshow(img)
plt.show()