import cv2
import numpy as np
from PIL import Image
import time
import math

# numpy.whereで合成する
#  他関数との関係上RGBA画像を取り込んでいるが
#  使うのはRGB要素のみでアルファ値は使っていない。
#  透明色(0,0,0)を決め打ちしているが良いやり方ではない。
def putSprite_npwhere(back, front4, pos):
    x, y = pos
    fh, fw = front4.shape[:2]
    bh, bw = back.shape[:2]
    x1, y1 = max(x, 0), max(y, 0)
    x2, y2 = min(x+fw, bw), min(y+fh, bh)
    if not ((-fw < x < bw) and (-fh < y < bh)) :
        return back
    front3 = front4[:, :, :3]
    front_roi = front3[y1-y:y2-y, x1-x:x2-x]
    roi = back[y1:y2, x1:x2]
    tmp = np.where(front_roi==(0,0,0), roi, front_roi)
    back[y1:y2, x1:x2] = tmp
    return back

# マスク処理する
#  マスク画像はRGBA画像から都度関数内で作成する。
#  あらかじめマスク画像を作っておいたほうが速いが、
#  こちらのほうが使いやすい。と思う。
def putSprite_mask(back, front4, pos):
    x, y = pos
    fh, fw = front4.shape[:2]
    bh, bw = back.shape[:2]
    x1, y1 = max(x, 0), max(y, 0)
    x2, y2 = min(x+fw, bw), min(y+fh, bh)
    if not ((-fw < x < bw) and (-fh < y < bh)) :
        return back
    front3 = front4[:, :, :3]
    mask1 = front4[:, :, 3]
    mask3 = 255 - cv2.merge((mask1, mask1, mask1))
    mask_roi = mask3[y1-y:y2-y, x1-x:x2-x]
    front_roi = front3[y1-y:y2-y, x1-x:x2-x]
    roi = back[y1:y2, x1:x2]
    tmp = cv2.bitwise_and(roi, mask_roi)
    tmp = cv2.bitwise_or(tmp, front_roi)
    back[y1:y2, x1:x2] = tmp
    return back

# PILで合成する　背景画像全体
def putSprite_pil_all(back, front4, pos):
    back_pil = Image.fromarray(back)
    front_pil = Image.fromarray(front4)
    back_pil.paste(front_pil, pos, front_pil)
    return np.array(back_pil, dtype = np.uint8)

# PILで合成する　背景画像内にある部分のみ
def putSprite_pil_roi(back, front4, pos):
    x, y = pos
    fh, fw = front4.shape[:2]
    bh, bw = back.shape[:2]
    x1, y1 = max(x, 0), max(y, 0)
    x2, y2 = min(x+fw, bw), min(y+fh, bh)
    if not ((-fw < x < bw) and (-fh < y < bh)) :
        return back
    back_roi_pil = Image.fromarray(back[y1:y2, x1:x2])
    front_pil = Image.fromarray(front4[y1-y:y2-y, x1-x:x2-x])
    back_roi_pil.paste(front_pil, (0,0), front_pil)
    back_roi = np.array(back_roi_pil, dtype = np.uint8)
    back[y1:y2, x1:x2] = back_roi
    return back

def main(func):
    filename_back = '../10_train1_640/train1_459.jpg'
    filename_front = '../50kiri/0.jpg'
    img_back = cv2.imread(filename_back)
    img_front = cv2.imread(filename_front, -1)
    bh, bw = img_back.shape[:2]
    xc, yc = bw*0.5, bh*0.5
    rx, ry = bw*0.3, bh*1.2
    cv2.putText(img_back, func, (20,bh-20), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255))

    ### 時間を計るのはここから
    start_time = time.time()

    for angle in range(-180, 180):
        back = img_back.copy()
        x = int(xc + rx * math.cos(math.radians(angle)))
        y = int(yc + ry * math.sin(math.radians(angle)))
        img = eval(func)(back, img_front, (x,y))

        #ここは必要に応じて有効にしたり無効にしたりする
        #cv2.imshow(func, img)
        #cv2.waitKey(1)

    elasped_time = time.time() - start_time
    ### ここまで

    print (f"{func} : {elasped_time} sec")    
    cv2.destroyAllWindows()

if __name__ == "__main__":
    funcs = ["putSprite_npwhere",
             "putSprite_mask",
             "putSprite_pil_all" ,
             "putSprite_pil_roi" ]
    for func in funcs:
        for i in range(10):
            main(func)