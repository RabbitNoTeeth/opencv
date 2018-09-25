import cv2
import numpy
from learning_opencv3_with_python.chapter2.cameo.utils import *


def strokeEdges(src, dst, blurKsize=7, edgeKsize=5):
    if blurKsize > 3:
        blurredSrc = cv2.medianBlur(src, blurKsize)  # 使用中值滤波进行去噪
        graySrc = cv2.cvtColor(blurredSrc, cv2.COLOR_BGR2GRAY)
    else:
        graySrc = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    cv2.Laplacian(graySrc, cv2.CV_8U, graySrc, ksize=edgeKsize)  # 使用拉普拉斯函数进行边缘检测
    normalizedInverseAlpha = (1.0 / 255) * (255 - graySrc)  # 进行归一化，是像素值在0-1之间
    channels = cv2.split(src)
    for channel in channels:
        channel[:] = channel * normalizedInverseAlpha  # 反转图像颜色，原像素值越大，乘积后新像素值越小，达到将边缘变黑，背景变白的效果
    cv2.merge(channels, dst)


# 通用的卷积滤波器
class VConvolutionFilter(object):

    def __init__(self, kernel):
        self._kernel = kernel

    def apply(self, src, dst):
        cv2.filter2D(src, -1, self._kernel, dst)


# 锐化滤波器
class SharpenFilter(VConvolutionFilter):

    def __init__(self):
        kernel = numpy.array([[-1, -1, -1],
                              [-1, 9, -1],
                              [-1, -1, -1]])
        VConvolutionFilter.__init__(self, kernel)


# 边缘检测滤波器
class FindEdgesFilter(VConvolutionFilter):

    def __init__(self):
        kernel = numpy.array([[-1, -1, -1],
                              [-1, 8, -1],
                              [-1, -1, -1]])
        VConvolutionFilter.__init__(self, kernel)


# 模糊滤波器(为了达到模糊的效果，通常权重和为1，并且邻近像素的权重全为正)
class BlurFilter(VConvolutionFilter):

    def __init__(self):
        kernel = numpy.array([[0.04, 0.04, 0.04, 0.04, 0.04],
                              [0.04, 0.04, 0.04, 0.04, 0.04],
                              [0.04, 0.04, 0.04, 0.04, 0.04],
                              [0.04, 0.04, 0.04, 0.04, 0.04],
                              [0.04, 0.04, 0.04, 0.04, 0.04]])
        VConvolutionFilter.__init__(self, kernel)


# 同时具有模糊和锐化效果的滤波器(通过不对称的卷积核)
class EmbossFilter(VConvolutionFilter):

    def __init__(self):
        kernel = numpy.array([[-2, -1, 0],
                              [-1, 1, 1],
                              [0, 1, 2]])
        VConvolutionFilter.__init__(self, kernel)