import os 
import glob
import sys


args = sys.argv
inpath = args[1]

sum_counter_0 = 0
sum_counter_1 = 0

folders = sorted(glob.glob(inpath + "/**/"))
for folder_path in folders:
    folder_name = os.path.basename(os.path.dirname(folder_path))
    files = glob.glob(inpath + "/" + folder_name + "/*.txt")
    counter_0 = 0
    counter_1 = 0
    for fname in files:
        if 'classes' in fname:
            continue
        with open(fname)as f:
            for line in f.readlines():
                if line[0] == '0':
                    counter_0 += 1
                else:
                    counter_1 += 1
        
    print("folder = {:<25}, counter_0 = {:<10}, counter_1 = {}".format(folder_name,counter_0,counter_1))
    sum_counter_0 += counter_0
    sum_counter_1 += counter_1

print("sum_counter_0 = {}, sum_counter_1 = {}".format(sum_counter_0,sum_counter_1))
