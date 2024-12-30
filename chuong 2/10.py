import json
import os
from collections import Counter

def employee_statistics(file_path):
    if not os.path.exists(file_path):
        print(f"Không tìm thấy file JSON tại đường dẫn: {file_path}")
        print("Vui lòng kiểm tra lại đường dẫn hoặc tên file.")
        return

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        company_name = data["company"]["name"]
        company_address = data["company"]["address"]
        
        departments = [emp["department"] for emp in data["employees"]]
        department_counts = Counter(departments)
        total_employees = len(data["employees"])

        print(f"Tên công ty: {company_name}")
        print(f"Địa chỉ: {company_address}")
        print(f"Tổng số nhân viên: {total_employees}\n")
        
        print("- Thống kê nhân viên theo đơn vị -")
        
        for i, (department, count) in enumerate(department_counts.items(), start=1):
            percentage = (count / total_employees) * 100
            print(f"{i}./Tên đơn vị: {department}")
            print(f"  Số nhân viên: {count}")
            print(f"  Tỷ lệ: {percentage:.2f}%\n")
    
    except json.JSONDecodeError:
        print("File JSON không hợp lệ. Vui lòng kiểm tra cấu trúc của file.")

file_path = "data.json"  
# Gọi hàm và truyền vào đường dẫn file JSON
employee_statistics(file_path)
employee_statistics("D:/btvn python kì 1/btvn_chương2/data.json")
