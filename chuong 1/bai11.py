import math

class TamGiac:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        if not self.kt():
            raise ValueError("Đây không phải là một tam giác hợp lệ")

    def kt(self):
        return (self.a + self.b > self.c and 
                self.a + self.c > self.b and 
                self.b + self.c > self.a)

    def chu_vi(self):
        return self.a + self.b + self.c

    def dien_tich(self):
        s = self.chu_vi() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def __str__(self):
        return f"Tam giác với các cạnh a={self.a}, b={self.b}, c={self.c}"


class TamGiacVuong(TamGiac):
    def __init__(self, a, b):
        c = math.sqrt(a**2 + b**2)
        super().__init__(a, b, c)
        if not self.vuong():
            raise ValueError("Đây không phải là tam giác vuông")

    def vuong(self):
        return math.isclose(self.a**2 + self.b**2, self.c**2)    #math.isclose so sánh 2 giá trị có bằng nhau không

    def __str__(self):
        return f"Tam giác vuông với các cạnh a={self.a}, b={self.b}, c={self.c}"


class TamGiacCan(TamGiac):
    def __init__(self, a, b):
        super().__init__(a, b, a)
        if not self.can():
            raise ValueError("Đây không phải là tam giác cân")

    def can(self):
        return self.a == self.b or self.a == self.c or self.b == self.c

    def __str__(self):
        return f"Tam giác cân với các cạnh a={self.a}, b={self.b}, c={self.c}"


class TamGiacDeu(TamGiacCan):
    def __init__(self, a):
        super().__init__(a, a)
        if not self.deu():
            raise ValueError("Đây không phải là tam giác đều")

    def deu(self):
        return self.a == self.b == self.c

    def __str__(self):
        return f"Tam giác đều với các cạnh bằng nhau a={self.a}, b={self.b}, c={self.c}"


# Ví dụ sử dụng các lớp
try:
    tam_giac_vuong = TamGiacVuong(3, 4)
    print(tam_giac_vuong)
    print(f"Chu vi: {tam_giac_vuong.chu_vi()}")
    print(f"Diện tích: {tam_giac_vuong.dien_tich()}")
except ValueError as e:     #nếu có lỗi thì sẽ lưu vào biến e và báo ra ko thì chạy bt
    print(e)

try:
    tam_giac_can = TamGiacCan(5, 8)
    print(tam_giac_can)
except ValueError as e:
    print(e)

try:
    tam_giac_deu = TamGiacDeu(6)
    print(tam_giac_deu)
    print(f"Chu vi: {tam_giac_deu.chu_vi()}")
    print(f"Diện tích: {tam_giac_deu.dien_tich()}")
except ValueError as e:
    print(e)
