import shutil
import os
import sys
import glob

args = sys.argv
org_section_paths = sorted(glob.glob('../org/**/'))
dstproject = args[1]
for org_section_path in org_section_paths:
    section = os.path.basename(os.path.dirname(org_section_path))
    filepaths = glob.glob(org_section_path + "/*")
    dst_dir_path = '../' + dstproject + '/' + section
    if not os.path.isdir(dst_dir_path):
        os.makedirs(dst_dir_path)
    for filepath in filepaths:
        if 'classes' in filepath:
            if os.path.isfile(dst_dir_path + 'classes.txt'):
                continue
        shutil.copy(filepath, dst_dir_path)
        


