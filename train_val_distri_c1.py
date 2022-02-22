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

sum_counter_0 = 0
sum_counter_1 = 0

folders = glob.glob(inpath + "/**/")
for folder_path in folders:
    folder_name = os.path.basename(os.path.dirname(folder_path))
    files = glob.glob(inpath + "/" + folder_name + "/*.txt")
    counter_0 = 0
    counter_1 = 0
    for fname in files:
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

val_limit_0 = sum_counter_0 / (trainwaruval + 1)
val_limit_1 = sum_counter_1 / (trainwaruval + 1)
print(val_limit_0)
print(val_limit_1)
counter_0 = 0
counter_1 = 0
flag = 'val'
for folder_path in folders:
    folder_name = os.path.basename(os.path.dirname(folder_path))
    txt_file_paths = glob.glob(inpath + "/" + folder_name + "/*.txt")
    for txt_file_path in txt_file_paths:
        if not 'classes' in txt_file_path:
            jpg_file_path = os.path.splitext(txt_file_path)[0] + ".jpg"
            with open(txt_file_path)as f:
                for line in f.readlines():
                    if line[0] == '0':
                        counter_0 += 1
                    else:
                        counter_1 += 1

            if flag == 'val':
                shutil.copy(txt_file_path, dst_val_path)
                shutil.copy(jpg_file_path, dst_val_path)
            else:
                shutil.copy(txt_file_path, dst_train_path)
                shutil.copy(jpg_file_path, dst_train_path)
    
    if counter_0 > val_limit_0:
        flag = 'train'