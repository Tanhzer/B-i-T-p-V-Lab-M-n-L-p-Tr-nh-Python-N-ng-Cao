import math

class Diem:
    def __init__(self):
        pass  # Không cần thuộc tính nào ở đây

class Elip(Diem):
    def __init__(self, ban_truc_lon, ban_truc_nho):
        super().__init__()
        self.ban_truc_lon = ban_truc_lon
        self.ban_truc_nho = ban_truc_nho

    def dien_tich(self):
        return math.pi * self.ban_truc_lon * self.ban_truc_nho

class HinhTron(Elip):
    pass

if __name__ == "__main__":
    ban_truc_lon = float(input("Nhập bán trục lớn của elip: "))
    ban_truc_nho = float(input("Nhập bán trục nhỏ của elip: "))
    elip = Elip(ban_truc_lon, ban_truc_nho)
    print(f"Diện tích elip: {elip.dien_tich():.2f}")