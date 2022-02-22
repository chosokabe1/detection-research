import cv2
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import glob
import itertools
import os
def binary(front):
    # front = cv2.cvtColor(front,cv2.COLOR_BGR2GRAY)
    ret, front_otsu = cv2.threshold(front, 180, 255,  cv2.THRESH_BINARY_INV)
    kernel1 = np.ones((5,5), np.uint8)
    kernel2 = np.ones((20,20), np.uint8)
    opening = cv2.morphologyEx(front_otsu, cv2.MORPH_OPEN, kernel1)
    opening_closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel2)
    return opening_closing

files = glob.glob('../50kiri_clear/*')
for file in files:
    img = cv2.imread(file,0)
    img = binary(img)
    cv2.imwrite('../50kiri_binary/' + os.path.basename(file), img)
