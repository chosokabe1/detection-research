import cv2
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import glob

def binary(front):
    ret, front_otsu = cv2.threshold(front, 0, 255,  cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    kernel = np.ones((5,5), np.uint8)
    opening = cv2.morphologyEx(front_otsu, cv2.MORPH_OPEN, kernel)
    opening_closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
    return opening_closing

def put_npwhere(back, mask, front, pos):
    x, y = pos
    fh, fw = front.shape[:2]
    bh, bw = back.shape[:2]
    x1, y1 = max(x, 0), max(y,0)
    x2, y2 = min(x+fw, bw), min (y+fh, bh)
    if not ((-fw < x < bw) and (-fh < y < bh)):
        return back
    back_roi = back[y1:y2, x1:x2]
    transparence = (0)
    mask_roi = mask[y1-y:y2-y, x1-x:x2-x]

    tmp = np.where(mask_roi==transparence, back_roi, mask_roi)

    back[y1:y2, x1:x2] = tmp
    return back


def itiren(path, pos):
    back = cv2.imread('../10_train1_640/train1_459.jpg', 0)
    front1 = cv2.imread(path, 0)
    binary_front1 = binary(front1)
    mask1 = cv2.bitwise_and(front1, binary_front1)
    # cv2.imshow('img3', mask1)

    small = put_npwhere(back, mask1, front1, pos)
    return back

paths = glob.glob('../50kiri/*')
dst = itiren(paths[0], (100,400))
cv2.imshow('img3', dst)
cv2.waitKey(0)