import os
import torch
import torch.nn as nn
import numpy as np
from src.model import MalConv
from torch.autograd import Variable

model = torch.load('../../checkpoint/test_case_1_sd_1.model', map_location=torch.device('cpu'), weights_only=False)

model.eval()

first_n_byte = 2000000
window_size = 500

sigmoid = nn.Sigmoid()

good_path = 'goodware/'
mal_path = 'malware/'
good_dir = os.listdir(good_path)
mal_dir = os.listdir(mal_path)

def predict(file_path, first_n_byte, indi):
    history = {}
    history['pred'] = []
    input_data = exe_data(file_path, first_n_byte)
    input_data = torch.tensor(input_data)

    print(input_data)
    with torch.no_grad():
        pred = model(input_data)    

    history['pred'].append(list(sigmoid(pred).cpu().numpy()))
    print(history)
    print(f'mal : {indi}\n')

def exe_data(file_path, first_n_byte):
    # 입력 파일을 읽어들여 바이너리 데이터를 텐서로 변환
    try:
        with open(file_path, 'rb') as f:
            tmp = [i+1 for i in f.read()[:first_n_byte]]
            tmp = tmp+[0]*(first_n_byte-len(tmp))
    except:
        with open(file_path.lower(), 'rb') as f:
            tmp = [i+1 for i in f.read()[:first_n_byte]]
            tmp = tmp+[0]*(first_n_byte-len(tmp))
        

    return np.array(tmp)


with open('./indi.txt', 'r') as file:
    content = file.readlines()

for con in content:
    con = con[:-1].split(' ')
    name = con[0]
    indi = con[1]
    
    for good_name in good_dir:
        if name == good_name:
            predict(good_path+good_name, first_n_byte, indi)

    for mal_name in mal_dir:
        if name == mal_name:
            predict(mal_path+mal_name, first_n_byte, indi)
            


