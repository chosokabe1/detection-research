import sys
import os 
import glob

args = sys.argv
inpath = args[1]

file_paths = sorted (glob.glob(inpath + "/*"))
for file_path in file_paths:
    filename = os.path.basename(file_path)
    other_file_path = os.path.join(os.path.dirname(file_path), '2_' + filename)
    os.rename(file_path, other_file_path)