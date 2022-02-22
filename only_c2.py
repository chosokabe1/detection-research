import cv2
import glob
import sys
import os
import shutil

only_c2_dir = '../only_contact'
bamen_paths = glob.glob(only_c2_dir + '/**/')
for bamen_path in bamen_paths:
    file_paths = glob.glob(bamen_path + "*")
    for file_path in file_paths:
        if 'classes' in file_path:
            os.remove(file_path)
            f = open(file_path, 'w')
            f.write('contact')
            f.close()
        
        if 'jpg' in file_path:
            continue
        
        if not 'classes' in file_path:
            f = open(file_path, 'r')
            datalist = f.readlines()
            f.close()
            nocontact = True
            for data in datalist:
                if(data[0] == '1'):
                    nocontact = False
                
            if nocontact:
                os.remove(file_path)
                os.remove(bamen_path + os.path.splitext(os.path.basename(file_path))[0] + '.jpg')
    
            if os.path.exists(file_path):
                with open(file_path, 'w') as f:
                    for data in datalist:
                        if data[0] != '0':
                            f.write('0' + data[1:])