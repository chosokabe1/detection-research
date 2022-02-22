import cv2
import glob
import os

txt_paths = sorted(glob.glob("../../bamenn_c2/kiri/4/*.txt"))
out_path = '../../bamenn_c2/cut/4'
if not os.path.exists(out_path):
    # ディレクトリが存在しない場合、ディレクトリを作成する
    os.makedirs(out_path)
count = 0
for txt_path in txt_paths:
    if 'classes' in txt_path:
        continue

    jpg_path = os.path.splitext(txt_path)[0] + '.jpg'
    print(jpg_path)

    img = cv2.imread(jpg_path, 0)
    with open(txt_path) as f:
        s = f.readlines()
        print(s)
        
        
        for line in s:
            split = line.split()
            if split:
                center_x_float = float(split[1])
                center_y_float = float(split[2])
                width_float    = float(split[3])
                height_float   = float(split[4])
    
                print(center_x_float)  
                print(center_y_float)
                print(width_float)  
                print(height_float)
                print(img.shape)
                center_x_int = round(img.shape[1] * center_x_float)
                center_y_int = round(img.shape[0] * center_y_float)
                width_int    = round(img.shape[1] * width_float)
                height_int   = round(img.shape[0] * height_float)
                kiri_left = center_x_int - width_int // 2
                kiri_right = kiri_left + width_int
                kiri_top = center_y_int - height_int // 2
                kiri_bottom = kiri_top + height_int
                kiri_img = img[kiri_top:kiri_bottom, kiri_left:kiri_right]
                cv2.imwrite(out_path + '/' + str(count) + '.jpg', kiri_img)
                count += 1 
    
    
