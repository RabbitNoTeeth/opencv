import cv2
import numpy as np


# 对原始图像进行向下取样，缩小分辨率
img = cv2.pyrDown(cv2.imread("C:/Users/LIUXINDONG/Desktop/opencv/images/chapter12/image/closing.bmp", cv2.IMREAD_UNCHANGED))
# 对图像进行二进制阈值化
ret, thresh = cv2.threshold(cv2.cvtColor(img.copy(), cv2.COLOR_BGR2GRAY), 127, 255, cv2.THRESH_BINARY)
# 找出外侧轮廓
image, contours, hier = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for c in contours:
    # 计算出一个简单的边界框
    x, y, w, h = cv2.boundingRect(c)
    # 将边界框画到图像上
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    # 计算出包围目标的最小矩形区域
    rect = cv2.minAreaRect(c)
    box = cv2.boxPoints(rect)
    bos = np.int0(box)
    # 画出改矩形
    cv2.drawContours(img, [box], 0, (0, 0, 255), 3)

    # 计算并画出最小闭圆
    (x, y), radius = cv2.minEnclosingCircle(c)
    center = (int(x), int(y))
    radius = int(radius)
    img = cv2.circle(img, center, radius, (0, 255, 0), 2)

cv2.drawContours(img, contours, -1, (255, 0, 0), 1)
cv2.imshow("contours", img)
