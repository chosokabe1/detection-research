import os 
import glob
import sys
import shutil

args = sys.argv
inpath = args[1]
trainwaruval = int(args[2])
classes = ['1','2']

dst_train_path = inpath + '_train'
dst_val_path   = inpath + '_val'

if not os.path.exists(dst_train_path):
    os.makedirs(dst_train_path)

if not os.path.exists(dst_val_path):
    os.makedirs(dst_val_path)

# f = open(dst_train + "/classes.txt", 'a')
# for class_name in classes:
#     f.write(class_name + "\n")

# f.colse()

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

print(counter_0)
print(counter_1)

sum_counter_0 = counter_0
sum_counter_1 = counter_1
val_limit_0 = sum_counter_0 / (trainwaruval + 1)
val_limit_1 = sum_counter_1 / (trainwaruval + 1)
print(val_limit_0)
print(val_limit_1)
counter_0 = 0
counter_1 = 0
txt_files_path = glob.glob(inpath + "/*.txt")
for txt_file_path in txt_files_path:
    if not 'classes' in txt_file_path:
        jpg_file_path = os.path.splitext(txt_file_path)[0] + ".jpg"
        with open(txt_file_path)as f:
            for line in f.readlines():
                if line[0] == '0':
                    counter_0 += 1
                else:
                    counter_1 += 1
                
        if counter_0 < val_limit_0:
            shutil.copy(txt_file_path, dst_val_path)
            shutil.copy(jpg_file_path, dst_val_path)
        else:
            shutil.copy(txt_file_path, dst_train_path)
            shutil.copy(jpg_file_path, dst_train_path)
    