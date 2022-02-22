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

if not os.path.exists(dstpath + '/classes.txt'):
    shutil.copy(inpath + '/classes.txt', dstpath)

files = glob.glob(inpath + "/*.txt")
for fname in files:
    if 'classes' in fname:
        continue

    shutil.copy(fname, dstpath)
    
    with open(fname) as f:
        lines = f.readlines()

    for line in lines:
        label = line[0]
        center_x = line[2:10]
        center_y = line[11:19]
        width = line[20:28]
        height = line[29:37]

        center_x_90 = str(round((1-float(center_y)), 6))
        if center_x_90 == 0:
            center_x_90 += '.'

        while len(center_x_90) < 8:
            center_x_90 += '0'

        while len(center_x_90) > 8:
            center_x_90 

        center_y_90 = center_x
        width_90    = height
        height_90   = width

        center_x_180 = str(round((1-float(center_x)), 6)) 
        if center_x_180 == 0:
            center_x_180 += '.'

        while len(center_x_180) < 8:
            center_x_180 += '0'

        center_y_180 = str(round((1-float(center_y)), 6)) 
        if center_y_180 == 0:
            center_y_180 += '.'

        while len(center_y_180) < 8:
            center_y_180 += '0'

        width_180 = width
        height_180 = height

        center_x_270 = center_y
        center_y_270 = str(round((1-float(center_x)), 6)) 
        if center_y_270 == 0:
            center_y_270 += '.'

        while len(center_y_270) < 8:
            center_y_270 += '0'

        width_270 = height
        height_270 = width

        f = open(dstpath + '/90rot_' + os.path.basename(fname), 'a')
        f.write(label + " " + center_x_90 + " " + center_y_90 + " " + width_90 + " " + height_90 + "\n")
        f.close()

        f = open(dstpath + '/180rot_' + os.path.basename(fname), 'a')
        f.write(label + " " + center_x_180 + " " + center_y_180 + " " + width_180 + " " + height_180 + "\n")
        f.close()

        f = open(dstpath + '/270rot_' + os.path.basename(fname), 'a')
        f.write(label + " " + center_x_270 + " " + center_y_270 + " " + width_270 + " " + height_270 + "\n")
        f.close()

files = sorted(glob.glob(inpath + "/*.jpg"))
for fname in files:
    img = cv2.imread(fname)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img90 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    img180 = cv2.rotate(img, cv2.ROTATE_180)
    img270 = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
    save_fname = fname.replace(inpath + '/', '')
    cv2.imwrite(dstpath + '/' + os.path.basename(fname), img) 
    cv2.imwrite(dstpath + '/90rot_' + os.path.basename(fname), img90) 
    cv2.imwrite(dstpath + '/180rot_' + os.path.basename(fname), img180) 
    cv2.imwrite(dstpath + '/270rot_' + os.path.basename(fname), img270) 

