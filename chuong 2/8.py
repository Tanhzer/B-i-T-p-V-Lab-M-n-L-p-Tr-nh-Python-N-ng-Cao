import json

if __name__ == "__main__":
    python_object = {
        "name": "PhngwTkao",
        "age": 18,
        "city": "VietNamese",
        "is_student": False,
        "grades": [95, 89, 78]
    }

    json_string = json.dumps(python_object, indent=2)
    print("Chuỗi JSON sau khi chuyển đổi:")
    print(json_string)