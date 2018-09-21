import cv2
import numpy as np
from scipy import ndimage


kernel_3x3 = np.array([[-1, -1, -1],
                       [-1, 8, -1],
                       [-1, -1, -1]])

kernel_5x5 = np.array([[-1, -1, -1, -1, -1],
                       [-1, 1, 2, 1, -1],
                       [-1, 2, 4, 2, -1],
                       [-1, 1, 2, 1, -1],
                       [-1, -1, -1, -1, -1]])

lena = cv2.imread("C:/Users/LIUXINDONG/Desktop/opencv/images/chapter6/image/lenacolor.png", 0)

k3 = ndimage.convolve(lena, kernel_3x3)
k5 = ndimage.convolve(lena, kernel_5x5)

blurred = cv2.GaussianBlur(lena, (11, 11), 0)
g_hpf = lena - blurred

cv2.imshow("k3", k3)
cv2.imshow("k5", k5)
cv2.imshow("g_hpf", g_hpf)
cv2.waitKey()
cv2.destroyAllWindows()
