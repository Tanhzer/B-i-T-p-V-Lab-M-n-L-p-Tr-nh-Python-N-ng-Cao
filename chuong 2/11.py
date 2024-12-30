import json
from datetime import datetime

class GiaoDich:
    def __init__(self, loai, so_luong, gia):
        self.loai = loai
        self.so_luong = so_luong
        self.gia = gia
        self.thanh_tien = so_luong * gia

    def to_dict(self):
        return {
            'loai': self.loai,
            'so_luong': self.so_luong,
            'gia': self.gia,
            'thanh_tien': self.thanh_tien
        }

ds_giao_dich = []

def thuc_hien_giao_dich():
    while True:
        loai = input("Nhập loại giao dịch (vàng/tiền): ")
        so_luong = int(input("Nhập số lượng: "))
        gia = float(input("Nhập giá: "))
        
        giao_dich = GiaoDich(loai, so_luong, gia)
        ds_giao_dich.append(giao_dich)
        
        tiep_tuc = input("Có muốn tiếp tục giao dịch không? (y/n): ")
        if tiep_tuc.lower() != 'y':
            break

def ghi_file_json():
    current_time = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    filename = f"{current_time}.json"

    data = [giao_dich.to_dict() for giao_dich in ds_giao_dich]

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print(f"Dữ liệu đã được ghi vào tập tin {filename}")

if __name__ == "__main__":
    thuc_hien_giao_dich()
    
    ghi_vao_file = int(input("Bạn có muốn ghi vào tập tin không? (1: Có, 0: Không): "))
    if ghi_vao_file == 1:
        ghi_file_json()
    else:
        print("Không ghi vào tập tin.")