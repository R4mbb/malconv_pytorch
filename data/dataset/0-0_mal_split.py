# malware 와 goodware를 나눔.
import os
import shutil
import json

sample_path = './sample/'
json_path = './json/'
sample_dir = os.listdir(sample_path)
json_dir = os.listdir(json_path)

mal_dir = './malware/'
good_dir = './goodware/'

try:
    os.mkdir(mal_dir)
    os.mkdir(good_dir)
except:
    pass

for json_name in json_dir:
    with open(json_path+json_name, 'r') as json_n:
        indicate = json.load(json_n)

    malware = indicate['malicious']
    goodware = indicate['undetected']

    sample_name = json_name.split('.')
    sample_name = sample_name[0]

    if malware >= 2:
        shutil.move(sample_path + sample_name, mal_dir + sample_name)
    else:
        shutil.move(sample_path + sample_name, good_dir + sample_name)
