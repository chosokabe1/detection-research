import cv2
import glob
import sys
import os

#resize 入力dir　出力dir サイズ
args = sys.argv
dstpath = args[2]
inpath = args[1]
size = args[3]

def scale_to_width(img, width):
    h, w = img.shape[:2]
    height = round(h * (width / w))
    dst = cv2.resize(img, dsize=(width, height))
    return dst
files = sorted(glob.glob(inpath + "/*.jpg"))
if not os.path.exists(dstpath):
    os.makedirs(dstpath)

for i,f_path in enumerate(files):
    img = cv2.imread(f_path)
    img = scale_to_width(img, int(size))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    fname = os.path.basename(f_path) 
    cv2.imwrite(dstpath + '/' + fname, img)
