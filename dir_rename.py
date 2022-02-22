import sys
import os 
import glob

args = sys.argv
inpath = args[1]

paths = glob.glob(inpath + '/*')
for path in paths:
    if "classes" in path:
        continue
    
    os.rename(path, os.path.dirname(path) + '/gousei_' + os.path.basename(path))

