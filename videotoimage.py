import cv2
import os
import glob
import sys

args = sys.argv
inpath = args[1]


def save_all_frames(video_path, dir_path, basename, ext='jpg'):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        return
    
    os.makedirs(dir_path, exist_ok=True)
    base_path = os.path.join(dir_path, basename)

    digit = len(str(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))))

    n = 0

    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imwrite('{}_{}.{}'.format(base_path, str(n).zfill(digit), ext), frame)
            n += 1
        else:
            return

img_fname = os.path.basename(inpath).replace('.mp4', '')
dir_name = img_fname + '_img'
if not os.path.exists(dir_name):
    os.mkdir(dir_name)

save_all_frames(inpath, dir_name, img_fname)


