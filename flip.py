import cv2
import glob
import sys
import os
import shutil

args = sys.argv
inpath = args[1]
dstpath = inpath + '_flip/'
if not os.path.exists(dstpath):
    os.makedirs(dstpath)

files = sorted(glob.glob(inpath + "/*"))
for i,file in enumerate(files):
    img = cv2.imread(file)
    img_flip_lr = cv2.flip(img, 1)
    cv2.imwrite(dstpath + i, img_flip_lr)

    
    