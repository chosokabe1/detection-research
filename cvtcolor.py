import cv2
import glob
import sys
import os

#cvtcolor 入力dir　出力dir
args = sys.argv
inpath = args[1]

def save_file(path, img):
    cv2.imwrite(path, img)

files = sorted(glob.glob(inpath + "/*.jpg"))

for i,fname in enumerate(files):
    img = cv2.imread(fname)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(fname, img)
