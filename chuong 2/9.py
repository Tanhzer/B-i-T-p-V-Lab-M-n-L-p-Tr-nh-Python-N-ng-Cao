import json

dict_obj = {
    "name": "PhuongThao",
    "age": 18,
    "city": "Pleiku",
    "job": "BA"
}

# Chuyển đổi từ điển thành JSON và in với thụt lề 4
json_data = json.dumps(dict_obj, indent=4, sort_keys=True)
print(json_data)
