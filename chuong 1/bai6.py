from bai4 import *
def print_stack(self):
        """In nội dung của ngăn xếp"""
        if self.isEmpty():
            print("Ngăn xếp rỗng.")
        else:
            print("Nội dung ngăn xếp:")
            for i in range(0, self.top + 1): 
                print(self.stack[i])