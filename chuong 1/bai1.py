class HCN:
    def __init__(self, chieu_rong, chieu_dai):
        self.chieu_rong = chieu_rong
        self.chieu_dai = chieu_dai

    def chu_vi(self):
        return (self.chieu_rong + self.chieu_dai) * 2

    def dien_tich(self):
        return self.chieu_rong * self.chieu_dai

    def in_thong_tin(self):
        print("Độ dài hai cạnh: chiều rộng =", self.chieu_rong, ", chiều dài =", self.chieu_dai)
        print("Chu vi hình chữ nhật là:", self.chu_vi())
        print("Diện tích hình chữ nhật là:", self.dien_tich())

def main():
    chieu_rong = float(input("Nhập chiều rộng của hình chữ nhật: "))
    chieu_dai = float(input("Nhập chiều dài của hình chữ nhật: "))

    hcn = HCN(chieu_rong, chieu_dai)
    hcn.in_thong_tin()

if __name__ == "__main__":
    main()
    
