import glob
import os
# section_paths = glob.glob('../synthetic/**/')
section_paths = ['../synthetic/26/']
for section_path in section_paths:
    file_paths = glob.glob(section_path + '*')
    for file_path in file_paths:     
        if 'classes' in file_path:
            continue
        dst_filename = 'synthetic_' + os.path.basename(os.path.dirname(section_path)) + '_' + os.path.basename(file_path)[7:]
        os.rename(file_path, section_path + dst_filename)
