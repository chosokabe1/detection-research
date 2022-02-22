import itertools
import cv2
import numpy as np

width = 640
height = 469

lists = list(range(0,3))
print(lists)
print(len(list(itertools.combinations(lists, 2))))

# for x in itertools.combinations(lists, 2):
#     print(x)

kumiawase = list(itertools.combinations(lists, 2))
print(kumiawase)
print(kumiawase[0][1])
for x in kumiawase:
    img1 = cv2.imread('../50kiri/' + str(x[0]) + '.jpg', 0)
    img2 = cv2.imread('../50kiri/' + str(x[1]) + '.jpg', 0)

    print(img1.shape)
    ret, img1_otsu = cv2.threshold(img1, 0, 255,  cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    ret, img2_otsu = cv2.threshold(img2, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    img1_mask = cv2.bitwise_and(img1, img1_otsu)
    cv2.imshow('img1_mask', img1_mask)
    cv2.waitKey(0)
    blank = np.zeros((height, width))
    blank += 255

    cv2.imwrite('blank.jpg', blank)
