import sys
import cv2
import shutil
import glob
import os

#第一引数 何名ごとか
#第二引数 入力ディレクトリ
#第三引数 出力ディレクトリ

args = sys.argv
inpath = args[2]
dstpath = args[3]

files = sorted(glob.glob(inpath + "/*"))
counter = 1
if not os.path.exists(dstpath):
    os.makedirs(dstpath)

for file in files:
    if counter == int(args[1]):
        shutil.copy(file, dstpath)
        counter = 1

    else:
        counter += 1
