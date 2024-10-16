# train과 valid로 나누는 마지막 과정.
# 만들어지는 train과 valid 내에서 다음 파일을 실행해야 함.
import os
import shutil

train_path = 'train/'
valid_path = 'valid/'

tr_good_path = 'goodware/'
tr_mal_path = 'malware/'
va_good_path = 'val_goodware/'
va_mal_path = 'val_malware/'

tr_good_dir = os.listdir(tr_good_path)
tr_mal_dir = os.listdir(tr_mal_path)
va_good_dir = os.listdir(va_good_path)
va_mal_dir = os.listdir(va_mal_path)

txt = 'train_result.txt'

try:
    os.mkdir(train_path)
    os.mkdir(valid_path)
except:
    pass


train_txt = open(train_path+txt, 'w')
valid_txt = open(valid_path+txt, 'w')

for good_filename in tr_good_dir:
    shutil.move(tr_good_path + good_filename, train_path + good_filename)
    good_filename = good_filename + ' 0\n'
    train_txt.write(good_filename)
for mal_filename in tr_mal_dir:
    shutil.move(tr_mal_path + mal_filename, train_path + mal_filename)
    mal_filename = mal_filename + ' 1\n'
    train_txt.write(mal_filename)
for good_filename in va_good_dir:
    shutil.move(va_good_path + good_filename, valid_path + good_filename)
    good_filename = good_filename + ' 0\n'
    valid_txt.write(good_filename)
for mal_filename in va_mal_dir:
    shutil.move(va_mal_path + mal_filename, valid_path + mal_filename)
    mal_filename = mal_filename + ' 1\n'
    valid_txt.write(mal_filename)

os.rmdir(tr_good_path)
os.rmdir(tr_mal_path)
os.rmdir(va_good_path)
os.rmdir(va_mal_path)
