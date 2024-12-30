class PS:
    def __init__(self, tu_so, mau_so):
        self.tu_so = tu_so
        self.mau_so = mau_so
        self.kt()

    def kt(self):
        if self.mau_so == 0:
            raise ValueError("Mẫu số không thể bằng 0.")
    
    def nhap(self):
        self.tu_so = float(input("Nhập tử số: "))
        self.mau_so = float(input("Nhập mẫu số: "))
        self.kt()

    def In(self):
        print(f"{int(self.tu_so)}/{int(self.mau_so)}")


