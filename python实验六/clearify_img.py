"""
自己找到一张因为光线太暗看不清的液晶照片，或者逆光拍摄曝光过度的照片，
使用opencv幂律变换对照片进行处理，让照片相对更清楚；
通过公式：
    当图像的整体灰度偏暗时，选择γ<1,可以使图像增亮
    当图像的整体灰度偏亮时，选择γ>1,可以使图像变暗
    提高图像的对比度，凸显细节。
"""
import cv2
import numpy as np


def gamma_correction(img, c=1, g=2.2):
    """
    opencv的幂次变换，y=cr^g
    :param img:输入图像
    :param c:公式参数
    :param g:公式参数
    :return:输出图像
    """
    out_img = img.copy()
    out_img /= 255.  # 归一化，限定在【0，1]范围内。
    out_img = (1 / c) * out_img ** (1 / g)  # 【0，1】内进行伽马变换
    out_img *= 255  # 之后变回来
    out_img = out_img.astype(np.uint8)  # 【0，255】整形
    return out_img


img = cv2.imread('2.jpg').astype(np.float)
init_img = cv2.imread('2.jpg')
out = gamma_correction(img)
new_img = np.hstack([init_img, out])
cv2.namedWindow("normal1", cv2.WINDOW_NORMAL)
cv2.imshow('normal1', new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
