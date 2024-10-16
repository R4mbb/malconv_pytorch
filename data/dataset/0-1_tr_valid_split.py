# train셋과 valid셋을 7:3 비율로 나눔.
import os
import shutil

mal_path = './malware/'
good_path = './goodware/'
valid_mal_path = './val_malware/'
valid_good_path = './val_goodware/'

mal_dir = os.listdir(mal_path)
good_dir = os.listdir(good_path)

try:
    os.mkdir(valid_mal_path)
    os.mkdir(valid_good_path)
except:
    pass


valid_len = len(mal_dir) // 10
valid_len = valid_len * 3

for num, mal_name in enumerate(mal_dir):
    shutil.move(mal_path + mal_name, valid_mal_path + mal_name)
    
    if num == valid_len:
        break

for num, good_name in enumerate(good_dir):
    shutil.move(good_path + good_name, valid_good_path + good_name)
    
    if num == valid_len:
        break
