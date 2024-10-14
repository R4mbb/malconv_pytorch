import torch
from src.model import MalConv
from src.util import ExeDataset,write_pred
from torch.utils.data import DataLoader


model = torch.load('model/example_sd_1.model', map_location=torch.device('cpu'), weights_only=False)
model.eval()

first_n_bytes = 20000000
file_path = 'data/ECEE659BBF94547F49CA8E8E38F067896BC7AB1FF8575A5D551DE1FD7D273D9F'

def preprocess_input(file_path, first_n_bytes):
    # 입력 파일을 읽어들여 바이너리 데이터를 텐서로 변환
    with open(file_path, 'rb') as f:
        byte_data = f.read()

    # 각 바이트 값을 정수로 변환하고 텐서로 변환
    input_data = torch.tensor([b for b in byte_data], dtype=torch.long)

    # 모델의 입력 크기에 맞게 크기 조정 (패딩 등 필요할 수 있음)
    input_data = input_data[:first_n_bytes]  # MalConv의 입력 크기에 맞춤

    # 텐서를 배치 차원 추가
    return input_data.unsqueeze(0)



input_data = preprocess_input(file_path, first_n_bytes)

with torch.no_grad():
    predict = model(input_data)

print("Predict : ", predict)
