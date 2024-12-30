import math

class DaGiac:
    def __init__(self, so_canh):
        self.so_canh = so_canh

class HinhBinhHanh(DaGiac):
    def __init__(self, day, cao):
        super().__init__(4)  # Hình bình hành có 4 cạnh
        self.day = day
        self.cao = cao

    def dien_tich(self):
        return self.day * self.cao

    def chu_vi(self):
        return 2 * (self.day + self.cao)

class HinhChuNhat(HinhBinhHanh):
    def __init__(self, rong, cao):
        super().__init__(rong, cao)

class HinhVuong(HinhChuNhat):
    def __init__(self, canh):
        super().__init__(canh, canh)

# Hàm chính để nhập và tính toán
def main():
    print("Chương trình tính chu vi và diện tích của các hình học.")
    
    # Hình bình hành
    day = float(input("Nhập chiều dài đáy của hình bình hành: "))
    cao = float(input("Nhập chiều cao của hình bình hành: "))
    hinh_binh_hanh = HinhBinhHanh(day, cao)
    print(f"Chu vi hình bình hành: {hinh_binh_hanh.chu_vi()}")
    print(f"Diện tích hình bình hành: {hinh_binh_hanh.dien_tich()}")

    # Hình chữ nhật
    rong = float(input("Nhập chiều rộng của hình chữ nhật: "))
    cao = float(input("Nhập chiều cao của hình chữ nhật: "))
    hinh_chu_nhat = HinhChuNhat(rong, cao)
    print(f"Chu vi hình chữ nhật: {hinh_chu_nhat.chu_vi()}")
    print(f"Diện tích hình chữ nhật: {hinh_chu_nhat.dien_tich()}")

    # Hình vuông
    canh = float(input("Nhập chiều dài cạnh của hình vuông: "))
    hinh_vuong = HinhVuong(canh)
    print(f"Chu vi hình vuông: {hinh_vuong.chu_vi()}")
    print(f"Diện tích hình vuông: {hinh_vuong.dien_tich()}")

if __name__ == "__main__":
    main()
