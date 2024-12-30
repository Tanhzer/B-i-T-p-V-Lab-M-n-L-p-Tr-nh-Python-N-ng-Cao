class TS:
    def __init__(self, ho_ten="", diem_toan=0, diem_ly=0, diem_hoa=0):
        self.ho_ten = ho_ten
        self.diem_toan = diem_toan
        self.diem_ly = diem_ly
        self.diem_hoa = diem_hoa

    def nhap_thong_tin(self):
        self.ho_ten = input("Nhập họ tên thí sinh: ")
        self.diem_toan = self.nhap_diem("Nhập điểm Toán: ")
        self.diem_ly = self.nhap_diem("Nhập điểm Lý: ")
        self.diem_hoa = self.nhap_diem("Nhập điểm Hóa: ")

    def nhap_diem(self, number):
        while True:
            try:
                diem = float(input(number))
                if 0 <= diem <= 10: 
                    return diem
                else:
                    print("Điểm phải nằm trong khoảng 0 đến 10. Vui lòng nhập lại.")
            except ValueError:
                print("Giá trị không hợp lệ. Vui lòng nhập lại.")

    def in_thong_tin(self):
        print(f"Họ tên thí sinh: {self.ho_ten}")
        print(f"Điểm Toán: {self.diem_toan}")
        print(f"Điểm Lý: {self.diem_ly}")
        print(f"Điểm Hóa: {self.diem_hoa}")

    def tinh_tong_diem(self):
        return self.diem_toan + self.diem_ly + self.diem_hoa


# Nhập thông tin thí sinh
def nhap_thi_sinh():
    ds_thi_sinh = []
    so_luong_thi_sinh = int(input("Nhập số lượng thí sinh: "))
    for _ in range(so_luong_thi_sinh):
        ts = TS()
        ts.nhap_thong_tin()
        ds_thi_sinh.append(ts)
    return ds_thi_sinh


# Lọc thí sinh trúng tuyển
def loc_thi_sinh(ds_thi_sinh, diem_chuan):
    return sorted(
        (ts for ts in ds_thi_sinh if ts.tinh_tong_diem() >= diem_chuan),
        key=lambda x: x.tinh_tong_diem(),
        reverse=True
    )
# sort phương thức sắp xếp danh sách tại chỗ. 
# reverse = True sắp xếp giảm dần
# reverse = False    tăng dần


# In danh sách thí sinh trúng tuyển
def in_thi_sinh_trung_tuyen(thi_sinh_trung_tuyen):
    print("\nDanh sách thí sinh trúng tuyển:")
    for ts in thi_sinh_trung_tuyen:
        ts.in_thong_tin()
        print(f"Tổng điểm: {ts.tinh_tong_diem()}")


def main():
    ds_thi_sinh = nhap_thi_sinh()
    diem_chuan = 20
    thi_sinh_trung_tuyen = loc_thi_sinh(ds_thi_sinh, diem_chuan)
    in_thi_sinh_trung_tuyen(thi_sinh_trung_tuyen)

if __name__ == "__main__":
    main()




  




