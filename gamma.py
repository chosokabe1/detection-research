import cv2
import glob
import sys
import os
import numpy as np

#contrast 入力dir　出力dir サイズ
# args = sys.argv
# dstpath = args[2]
# inpath = args[1]


gamma1  = 1.5
LUT_G1 = np.arange(256, dtype = 'uint8')

for i in range(256):
    LUT_G1[i] = 255 * pow(float(i) / 255, 1.0 / gamma1)





src = cv2.imread("../640g20t26_30_c2/train26_079.jpg")
gamma_img = cv2.LUT(src, LUT_G1)
cv2.imwrite("../640g20t26_30_c2/train26_079.jpg", gamma_img)