"""
尝试编写一个程序，
让四川轻化工大学校徽图案中的黑色字体变成蓝色、红色、粉色、紫色等任意颜色，
或者将深绿色的圈和中央背景区变成 红色、橙色、黄色、紫色等颜色；
"""
import cv2 as cv
import numpy as np

str_color = input("请输入想变换的颜色:【黑色字体-->[蓝色、红色、粉色、紫色]】")
if str_color == '蓝色':
    conv_color = (158,160,95)
if str_color == '红色':
    conv_color = (0, 0, 255)
if str_color == '粉色':
    conv_color = (192, 203,255)
if str_color == '紫色':
    conv_color = (128, 0, 128)
init_img = cv.imread("mark.jpg")
img_info = init_img.shape
# print(img_info)
height = img_info[0]  # 424
width = img_info[1]  # 431
out = np.zeros((height, width, 3), np.uint8)  # 创建一个shape相同的空图像
temp = init_img.copy()
for h in range(0, height):
    for w in range(0, width):
        (b, g, r) = temp[h, w]  # OpenCV读取的图片格式为BGR格式，非RGB格式
        if (46, 255, 180) > (b, g, r) > (0, 0, 0):  # 设定黑色像素范围
            temp[h, w] = conv_color
        out[h, w] = temp[h, w]

cv.namedWindow("res", cv.WINDOW_NORMAL)
res = np.hstack([init_img, out])
cv.imshow("res", res)
cv.waitKey(0)
cv.destroyAllWindows()
