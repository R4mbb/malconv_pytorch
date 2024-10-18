# malware 개수에 맞춰서 goodware를 넣어준다.
# 경로랑 개수만 수정하면 됨.
import os
import shutil

gw_path = '../../goodware/'
ex_path = 'extract_3/'
ex_dir = os.listdir(ex_path)

for num, filename in enumerate(ex_dir):
    shutil.copy(ex_path+filename, gw_path+filename)

    if num == 533:
        break
