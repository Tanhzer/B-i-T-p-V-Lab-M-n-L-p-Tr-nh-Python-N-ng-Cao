class Stack:
    def __init__(self, capacity):
        #Hàm tạo
        self.capacity = capacity #sức chứa
        self.stack = [] 
        self.top = -1 

    def __del__(self):
        #Hàm hủy
        print("Ngăn xếp đã được giải phóng")

    def push(self, value):
        #Đưa một phần tử vào ngăn xếp
        if self.isFull():
            print("Ngăn xếp đầy, không thể thêm phần tử!")
        else:
            self.stack.append(float(value))
            self.top += 1

    def pop(self):
        #Lấy một phần tử ra từ đỉnh ngăn xếp
        if self.isEmpty():
            print("Ngăn xếp rỗng, không thể lấy phần tử!")
            return None
        else:
            self.top -= 1
            return self.stack.pop()

    def isEmpty(self):
        #Kiểm tra ngăn xếp có trống không
        return self.top == -1

    def isFull(self):
        #Kiểm tra ngăn xếpn đã đầy chưa
        return self.top == self.capacity - 1

# ví dụ
stack = Stack(3)
stack.push(1.1)
stack.push(2.2)
stack.push(3.3)

print("Pop:", stack.pop()) 
stack.push(4.4) 
print("Ngăn xếp rỗng?", stack.isEmpty())
print("Ngăn xếp đầy?", stack.isFull())

del stack 
