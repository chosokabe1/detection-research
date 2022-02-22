import cv2
import glob
import sys
import os
import numpy as np

#contrast 入力dir　出力dir サイズ
# args = sys.argv
# dstpath = args[2]
# inpath = args[1]

min_table = 50
max_table = 205
diff_table = max_table - min_table

LUT_HC = np.arange(256, dtype = 'uint8')

for i in range(0, min_table):
    LUT_HC[i] = 0
for i in range(min_table, max_table):
    LUT_HC[i] = 255 * (i - min_table) / diff_table
for i in range(max_table, 255):
    LUT_HC[i] = 255

src = cv2.imread("../640g20t26_30_c2/train26_079.jpg")
high_cont_img = cv2.LUT(src, LUT_HC)
cv2.imwrite("../640g20t26_30_c2/train26_079.jpg", high_cont_img)