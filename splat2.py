import os 
import glob
import sys
import shutil


#classesをのぞいて

args = sys.argv
inpath = args[1]

duplicatecount = 0
tvt_folder_paths = glob.glob(inpath + "/**/")
for tvt_folder_path in tvt_folder_paths:
    folder_paths = glob.glob(tvt_folder_path + "/**/")
    for folder_path in folder_paths:
        file_paths = glob.glob(folder_path + "/*")
        for file_path in file_paths:
            if 'classes' in file_path:
                if os.path.isfile(tvt_folder_path + 'classes.txt'):
                    continue
            if os.path.isfile(tvt_folder_path + '/' + os.path.basename(file_path)):
                duplicatecount += 1

            shutil.copy(file_path, tvt_folder_path)

for tvt_folder_path in tvt_folder_paths:
    folder_paths = glob.glob(tvt_folder_path + "/**/")
    count = 0
    for folder_path in folder_paths:
        shutil.rmtree(folder_path)


if not duplicatecount == 0:
    print('error There is ' + str(duplicatecount) + ' duplicatefilename')