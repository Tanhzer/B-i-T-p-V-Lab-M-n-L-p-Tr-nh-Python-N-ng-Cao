import tkinter as tk
from tkinter import messagebox
import sqlite3

# Kết nối tới cơ sở dữ liệu SQLite
def connect_db():
    conn = sqlite3.connect("products.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# Thêm sản phẩm vào cơ sở dữ liệu
def add_product():
    name = entry_name.get()
    price = entry_price.get()
    if not name or not price:
        messagebox.showwarning("Lỗi", "Vui lòng nhập đầy đủ thông tin!")
        return
    try:
        conn = sqlite3.connect("products.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO products (name, price) VALUES (?, ?)", (name, float(price)))
        conn.commit()
        conn.close()
        entry_name.delete(0, tk.END)
        entry_price.delete(0, tk.END)
        load_products()
        messagebox.showinfo("Thành công", "Thêm sản phẩm thành công!")
    except ValueError:
        messagebox.showerror("Lỗi", "Giá sản phẩm phải là số!")

# Hiển thị danh sách sản phẩm
def load_products():
    listbox_products.delete(0, tk.END)
    conn = sqlite3.connect("products.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM products")
    rows = cur.fetchall()
    conn.close()
    for row in rows:
        listbox_products.insert(tk.END, f"{row[0]} - {row[1]} - {row[2]} VNĐ")

# Xóa sản phẩm khỏi cơ sở dữ liệu
def delete_product():
    selected_item = listbox_products.curselection()
    if not selected_item:
        messagebox.showwarning("Lỗi", "Vui lòng chọn sản phẩm để xóa!")
        return
    product_info = listbox_products.get(selected_item).split(" - ")
    product_id = product_info[0]
    conn = sqlite3.connect("products.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM products WHERE id = ?", (product_id,))
    conn.commit()
    conn.close()
    load_products()
    messagebox.showinfo("Thành công", "Xóa sản phẩm thành công!")

# Cập nhật sản phẩm
def update_product():
    selected_item = listbox_products.curselection()
    if not selected_item:
        messagebox.showwarning("Lỗi", "Vui lòng chọn sản phẩm để cập nhật!")
        return
    product_info = listbox_products.get(selected_item).split(" - ")
    product_id = product_info[0]
    new_name = entry_name.get()
    new_price = entry_price.get()
    if not new_name or not new_price:
        messagebox.showwarning("Lỗi", "Vui lòng nhập đầy đủ thông tin để cập nhật!")
        return
    try:
        conn = sqlite3.connect("products.db")
        cur = conn.cursor()
        cur.execute("UPDATE products SET name = ?, price = ? WHERE id = ?", (new_name, float(new_price), product_id))
        conn.commit()
        conn.close()
        load_products()
        messagebox.showinfo("Thành công", "Cập nhật sản phẩm thành công!")
    except ValueError:
        messagebox.showerror("Lỗi", "Giá sản phẩm phải là số!")

# Tạo cửa sổ chính
connect_db()
root = tk.Tk()
root.title("Quản lý sản phẩm")

# Widgets
label_name = tk.Label(root, text="Tên sản phẩm:")
label_name.grid(row=0, column=0, padx=10, pady=5)

entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=5)

label_price = tk.Label(root, text="Giá sản phẩm:")
label_price.grid(row=1, column=0, padx=10, pady=5)

entry_price = tk.Entry(root)
entry_price.grid(row=1, column=1, padx=10, pady=5)

button_add = tk.Button(root, text="Thêm", command=add_product)
button_add.grid(row=2, column=0, padx=10, pady=5)

button_update = tk.Button(root, text="Cập nhật", command=update_product)
button_update.grid(row=2, column=1, padx=10, pady=5)

button_delete = tk.Button(root, text="Xóa", command=delete_product)
button_delete.grid(row=2, column=2, padx=10, pady=5)

listbox_products = tk.Listbox(root, width=50)
listbox_products.grid(row=3, column=0, columnspan=3, padx=10, pady=5)

# Load dữ liệu ban đầu
load_products()

# Chạy ứng dụng
root.mainloop()