import cv2
import glob
import sys
import os

args = sys.argv
inpath = args[1]
dstpath = args[2]

if not os.path.exists(dstpath):
    os.makedirs(dstpath)

file_paths = glob.glob(inpath + "/*")
for i,file_path in enumerate(file_paths):
    img = cv2.imread(file_path,0)
    h, w = img.shape
    long_side = 'width'
    if(h >= w):
        long_side = 'height'
    
    if(long_side == 'width'):
        img2 = cv2.resize(img, (int(w*1.2), h))
        cv2.imwrite(dstpath + '/' + str(i) + '.jpg',img2)
        img2 = cv2.resize(img, (int(w*0.8), h))
        cv2.imwrite(dstpath + '/' + str(i) + '_2.jpg',img2)

    else:
        img2 = cv2.resize(img, (w, int(h*1.2)))
        cv2.imwrite(dstpath + '/' + str(i) + '.jpg',img2)
        img2 = cv2.resize(img, (w, int(h*0.8)))
        cv2.imwrite(dstpath + '/' + str(i) + '_2.jpg',img2)
