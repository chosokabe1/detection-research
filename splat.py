import os 
import glob
import sys
import shutil

#入力ディレクトリ以下のファイルを出力ディレクトリにぶちまける
#classesをのぞいて

args = sys.argv
inpath = args[1]
dstpath = inpath

if not os.path.exists(dstpath):
    os.makedirs(dstpath)

folders = glob.glob(inpath + "/**/")
for folder_path in folders:
    folder_name = os.path.basename(os.path.dirname(folder_path))
    files_path = glob.glob(folder_path + "/*")
    for file_path in files_path:
        if 'classes' in file_path:
            continue
            
        shutil.copy(file_path, dstpath)