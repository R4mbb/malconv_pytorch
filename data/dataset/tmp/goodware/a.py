import os
import shutil

gw_path = '../../goodware/'
ex_path = 'extract_3/'
ex_dir = os.listdir(ex_path)

for num, filename in enumerate(ex_dir):
    shutil.copy(ex_path+filename, gw_path+filename)

    if num == 533:
        break
