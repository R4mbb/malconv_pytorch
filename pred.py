import torch
import torch.nn as nn
import numpy as np
from src.model import MalConv
from torch.autograd import Variable

model = torch.load('checkpoint/test_case_1_sd_1.model', map_location=torch.device('cpu'), weights_only=False)

model.eval()

first_n_byte = 2000000
window_size = 500
file_path = 'data/valid/6BEA57FB8DFB41779AE842E8B3529933RUNTIMEDEVICEINSTALL74FEAF2D9C8B886EF65CBECFB0370840'
history = {}
history['pred'] = []


sigmoid = nn.Sigmoid()

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


input_data = exe_data(file_path, first_n_byte)
input_data = torch.tensor(input_data)

print(input_data)
with torch.no_grad():
    pred = model(input_data)    

history['pred'].append(list(sigmoid(pred).cpu().numpy()))
print(history)
