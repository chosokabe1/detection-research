# -*- coding: utf-8 -*-
import cv2
import glob
import sys
import os
import shutil


args = sys.argv
inpath = args[1]
dstpath = args[2]

if not os.path.exists(dstpath):
    os.makedirs(dstpath)

folder_paths = glob.glob(inpath + "/**/")
for folder_path in folder_paths:
    file_paths = glob.glob(folder_path + "*")
    for file_path in file_paths:
        if 'classes' in file_path:
            continue
        
        if 'jpg' in file_path:
            shutil.copy(file_path, dstpath)
            continue
        
        else:
            fname = os.path.basename(file_path)
            with open(file_path) as f:
                lines = f.readlines()
            
            
            # lineの先頭を0にする

            for line in lines:
                line = '0' + line[1:]
                with open(dstpath + "/" + fname, mode = 'a') as f:
                    f.write(line)
            











