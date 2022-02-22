import cv2
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import glob
import itertools
import os
import sys
import random
import shutil

args = sys.argv
inpath = args[1]
dstpath = args[2]
if not os.path.isdir(dstpath):
    os.makedirs(dstpath)

back_shape = (640,469)
back_path = '../back/6_1.jpg'
back_img = []

img = cv2.imread(back_path,0)
img = cv2.resize(img, dsize=back_shape)
back_img.append(img)

img_flip_ud = cv2.flip(img, 0)
back_img.append(img_flip_ud)

img_flip_lr = cv2.flip(img, 1)
back_img.append(img_flip_lr)

img_flip_ud_lr = cv2.flip(img, -1)
back_img.append(img_flip_ud_lr)

def kumiawase(number):
    lists = list(range(0,number))
    kumiawase = list(itertools.combinations(lists, 2))
    return kumiawase

def binary(front):
    # front = cv2.cvtColor(front,cv2.COLOR_BGR2GRAY)
    ret, front = cv2.threshold(front, 30, 255,  cv2.THRESH_BINARY)
    # kernel = np.ones((10,10), np.uint8)
    # kernel1 = np.ones((20,20), np.uint8)
    kernel = np.ones((3,3),np.uint8)
    erosion = cv2.erode(front,kernel,iterations = 1)
    # opening = cv2.morphologyEx(front, cv2.MORPH_OPEN, kernel)
    # opening_closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel1)
    return erosion

def put_npwhere(back, mask, front, pos):
    x, y = pos
    fh, fw = front.shape[:2]
    bh, bw = back.shape[:2]
    x1, y1 = max(x, 0), max(y,0)
    x2, y2 = min(x+fw, bw), min (y+fh, bh)
    if not ((-fw < x < bw) and (-fh < y < bh)):
        return back
    back_roi = back[y1:y2, x1:x2]
    mask_roi = mask[y1-y:y2-y, x1-x:x2-x]
    transparence = (0)
    tmp = np.where(mask_roi==transparence, back_roi, mask_roi)
    back[y1:y2, x1:x2] = tmp

    return back, x1, y1, x2, y2


#append_nematodeに入れるposは(x座標，y座標)
def append_nematode(back, nematode_path, pos):
    nema_img = cv2.imread(nematode_path)
    nema_img = cv2.cvtColor(nema_img, cv2.COLOR_BGR2GRAY)
    binary_nema = binary(nema_img)
    mask1 = cv2.bitwise_and(nema_img, binary_nema)
    back, left, top, right, bottom = put_npwhere(back, mask1, nema_img, pos)
    return back, left, top, right, bottom

def ketasoroe(ketasoroe, shousuutennika):
    if ketasoroe == '0':
        ketasoroe += '.'
    # print('s')
    while len(ketasoroe) < shousuutennika + 2:
        ketasoroe += '0'
    # print('b')
    while len(ketasoroe) > shousuutennika + 2:
        ketasoroe = ketasoroe[:8]
    
    # print('a')
    
    return ketasoroe


def make_anofile(dst_ano_path, back, left, top, right, bottom):
    bh = back.shape[0]
    bw = back.shape[1]
    
    #アノテーションの情報
    center_x = (left + right) / (2 * bw)#アノテーションのxの真ん中座標
    center_y = (top + bottom) / (2 * bh) #アノテーションのxの真ん中座標
    width = (right - left) / bw
    height = (bottom - top) / bh

    dst_center_x = ketasoroe(str(center_x), 6)
    dst_center_y = ketasoroe(str(center_y), 6)
    dst_width = ketasoroe(str(width), 6)
    dst_height = ketasoroe(str(height), 6)

    label = '1'
    f = open(dst_ano_path, 'a')
    f.write(label + " " + dst_center_x + " " + dst_center_y + " " + dst_width + " " + dst_height + "\n")
    f.close()

def nema_put_ope(img_paths, kumiawase):
    back = back_img[random.randint(0,len(back_img))].copy()
    #bh = back_height
    bh = back.shape[0]
    bw = back.shape[1]
    # backを縦2横3の6分割する
    sh = int(bh / 2)
    sw = int(bw / 3)
    #secposは(y座標,x座標)
    secpos = ((0,0),(0,sw),(0,2*sw),(sh,0),(sh,sw),(sh,2*sw))
    section = 0
    dst_img_number = 0
    for kumi in kumiawase:
        if section == 6:
            cv2.imwrite(dst_img_path, back)
            dst_img_number += 1
            section = 0
            back = back_img[random.randint(0,len( back_img ) - 1 )].copy()
            
        dst_img_path = dstpath + '/gousei_' + str(dst_img_number) + '.jpg'
        dst_ano_path = dstpath + '/gousei_' + str(dst_img_number) + '.txt'
        nema1_path = img_paths[kumi[0]]
        nema2_path = img_paths[kumi[1]]
        nema1_img  = cv2.imread(nema1_path)
        neam2_img  = cv2.imread(nema2_path)
        back, left, top, right, bottom = append_nematode(back, nema1_path, (secpos[section][1],secpos[section][0]))
        make_anofile(dst_ano_path, back, left, top, right, bottom)
        back, left, top, right, bottom = append_nematode(back, nema2_path, (secpos[section][1],secpos[section][0]))
        make_anofile(dst_ano_path, back, left, top, right, bottom)

        section += 1

    cv2.imwrite(dst_img_path, back)
    return back



txt_files = glob.glob(dstpath + '/*.txt')
for txt_file in txt_files:
    if 'class' in txt_file:
        continue

    os.remove(txt_file)

img_paths = glob.glob(inpath + '/*.jpg')


kumiawase = kumiawase(len(img_paths))
random.shuffle(kumiawase)
back = nema_put_ope(img_paths, kumiawase)
shutil.copy('../back/classes.txt', dstpath)




