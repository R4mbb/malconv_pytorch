# json이 없는 goodware 때문에 만듬.
# malware와 goodware가 나누어 졌을 때 json이 없는 goodware를 보충해서 
# 넣은 다음 해당 파일 돌리면 된다.
import os

goodware_path = 'goodware/'
malware_path = 'malware/'
goodware_dir = os.listdir(goodware_path)
malware_dir = os.listdir(malware_path)

file = open('indi.txt', 'w')

for good_name in goodware_dir:
    good_name = good_name + ' 0\n'
    file.write(good_name)

for mal_name in malware_dir:
    mal_name = mal_name + ' 1\n'
    file.write(mal_name)


