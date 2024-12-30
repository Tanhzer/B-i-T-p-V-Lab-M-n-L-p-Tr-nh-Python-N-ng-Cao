from bai7 import Date

class Employee:
    def __init__(self, ho_ten, ngay_sinh: Date, ngay_vao_cty: Date):
        self.ho_ten = ho_ten
        self.ngay_sinh = ngay_sinh
        self.ngay_vao_cty = ngay_vao_cty

    # Hiển thị thông tin nhân viên
    def display(self):
        print(f"Họ tên: {self.ho_ten}")
        print("Ngày sinh: ", end="")
        self.ngay_sinh.display()
        print("Ngày vào công ty: ", end="")
        self.ngay_vao_cty.display()

# Chương trình quản lý nhân viên
class QuanLyNhanVien:
    def __init__(self):
        self.danh_sach_nv = []

    # Thêm nhân viên
    def them_nhan_vien(self, nhan_vien: Employee):
        self.danh_sach_nv.append(nhan_vien)

    # Hiển thị 
    def hien_thi_nhan_vien(self):
        if not self.danh_sach_nv:
            print("Danh sách nhân viên trống.")
        else:
            for id, nv in enumerate(self.danh_sach_nv, 1):  #hiển thị danh sách thêm thứ tự nhập vào
                print(f"Nhân viên {id}:")                #enumerate duyệt qua từng đối tương có trong ds
                nv.display()
                print("-" * 27)

    # Xóa nhân viên 
    def xoa_nhan_vien(self, id):
        if 1 <= id < len(self.danh_sach_nv):
            self.danh_sach_nv.pop(id)   # pop loại bỏ phần tử ra khỏi ds
            print("Đã xóa nhân viên thành công.")
        else:
            print("Vị trí không hợp lệ!")

def menu():
    quan_ly = QuanLyNhanVien()

    while True:
        print("\nQuản lý nhân viên:")
        print("1. Hiển thị danh sách nhân viên ")
        print("2. Thêm nhân viên")
        print("3. Xóa nhân viên ")
        print("4. Thoát")
        
        choice = input("Chọn một tùy chọn: ")

        if choice == '1':
            quan_ly.hien_thi_nhan_vien()

        elif choice == '2':
            ho_ten = input("Nhập họ tên nhân viên: ")

            # Nhập ngày sinh
            day = int(input("Nhập ngày sinh: "))
            month = int(input("Nhập tháng sinh: "))
            year = int(input("Nhập năm sinh: "))
            ngay_sinh = Date(day, month, year)

            # Nhập ngày vào công ty
            day = int(input("Nhập ngày vào công ty: "))
            month = int(input("Nhập tháng vào công ty: "))
            year = int(input("Nhập năm vào công ty: "))
            ngay_vao_cty = Date(day, month, year)

            nhan_vien = Employee(ho_ten, ngay_sinh, ngay_vao_cty)
            quan_ly.them_nhan_vien(nhan_vien)

        elif choice == '3':
            quan_ly.hien_thi_nhan_vien()
            index = int(input("Nhập vị trí nhân viên muốn xóa (1, 2, 3,...): ")) - 1   # - 1 đi cho đúng thứ tự trong ds
            quan_ly.xoa_nhan_vien(id)

        elif choice == '4':
            print("Chương trình kết thúc.")
            break

        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại!")

menu()
