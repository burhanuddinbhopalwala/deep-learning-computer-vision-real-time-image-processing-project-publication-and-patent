import cv2
import os
import numpy as np

img1 = cv2.imread("W:\\MAJORPROJECt\\Python\\MajorProje\\funny\\f2.jpg")

cv2.namedWindow('dst_rt', cv2.WINDOW_NORMAL)


cv2.imshow('dst_rt', img1)
cv2.waitKey(0)

