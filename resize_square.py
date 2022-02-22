import cv2
import sys
import numpy as np

args = sys.argv

size = int(args[1])

def scale_to_width(img, width):
    h, w = img.shape[:2]
    height = round(h * (width / w))
    dst = cv2.resize(img, dsize=(width, height))
    return dst

img = cv2.imread('../10_train1_640/train1_019.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_gray = scale_to_width(img_gray, size)

img_white = np.zeros((size,size), np.unit8) * 255


cv2.imwrite('../640g10t1/019.jpg', img_gray)