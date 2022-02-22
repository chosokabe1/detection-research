import cv2
import glob
import sys
import os
import numpy as np
import shutil


args = sys.argv
inpath = args[1]
dstpath = args[2]

if not os.path.exists(dstpath):
    os.makedirs(dstpath)

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

gamma1  = 1.5
LUT_G1 = np.arange(256, dtype = 'uint8')

for i in range(256):
    LUT_G1[i] = 255 * pow(float(i) / 255, 1.0 / gamma1)

files = glob.glob(inpath + "/*.jpg")
for fname in files:
    src = cv2.imread(fname)
    
    dst = cv2.LUT(src, LUT_G1)
    dst = cv2.LUT(dst, LUT_HC)
    save_fname = os.path.basename(fname)
    cv2.imwrite(dstpath + "/con_" + save_fname, dst)

files = glob.glob(inpath + "/*.txt")
for fname in files:
    if 'classes' in fname:
        shutil.copy(fname, dstpath)

        continue

    shutil.copy(fname, dstpath + '/con_' + os.path.basename(fname))





