class ElectricBill:
    def __init__(self, ma_hoa_don, ten_KH, so_dien_sd, muc_gia):
        self.ma_hoa_dơn = ma_hoa_don
        self.ten_KH = ten_KH
        self.so_dien_sd = so_dien_sd
        self.muc_gia = muc_gia
    
    def calculate_total(self):
        return self.so_dien_sd* self.muc_gia
    
    def suggest_saving(self):
        suggestions = [
            "1. Sử dụng bóng đèn LED thay vì bóng đèn thường để tiết kiệm điện.",
            "2. Tắt các thiết bị điện khi không sử dụng, đặc biệt là ti vi, máy lạnh và quạt.",
            "3. Điều chỉnh nhiệt độ máy lạnh ở mức 25-27 độ C để tiết kiệm điện.",
            "4. Sử dụng thiết bị điện có nhãn năng lượng tiết kiệm.",
            "5. Lắp đặt hệ thống cách nhiệt cho nhà để giảm sử dụng máy lạnh.",
            "6. Tận dụng ánh sáng tự nhiên vào ban ngày thay vì bật đèn.",
            "7. Rút phích cắm của các thiết bị điện khi không sử dụng, vì chúng vẫn tiêu tốn điện năng."
        ]
        return suggestions