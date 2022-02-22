import os 
import glob
import sys


args = sys.argv
inpath = args[1]

counter_0 = 0
counter_1 = 0

files = glob.glob(inpath + "/*.txt")
for fname in files:
    with open(fname)as f:
        for line in f.readlines():
            if line[0] == '0':
                counter_0 += 1
            else:
                counter_1 += 1

print("counter_0 = {}, counter_1 = {}".format(counter_0,counter_1))
