# Bài 30: Class và Object (Lớp và Đối tượng)

# Khai báo class Car (Lớp Car – bản thiết kế cho một chiếc xe)
class Car:
    # Hàm khởi tạo (constructor)
    # Hàm này sẽ được gọi tự động mỗi khi tạo object mới từ class Car
    def __init__(self, name, brand, color):
        # self đại diện cho chính object đang được tạo
        # Gán giá trị truyền vào cho các thuộc tính của object
        self.name = name      # tên xe (vd: KIA Morning)
        self.brand = brand    # hãng xe (vd: KIA, Ferrari)
        self.color = color    # màu xe

    # Phương thức drive – hành động của xe
    def drive(self):
        # Sử dụng f-string để in thông tin của chính object đang gọi method
        print(
            f"Bạn đang lái chiếc xe {self.name} "
            f"màu {self.color} "
            f"của hãng xe {self.brand}"
        )


# ====== TẠO OBJECT (ĐỐI TƯỢNG) ======

# Tạo object kiaMorning từ class Car
# Khi dòng này chạy:
# 1. Python tạo object mới
# 2. Gọi hàm __init__
# 3. Gán:
#    self.name = "KIA Morning"
#    self.brand = "KIA"
#    self.color = "Xanh dương"
kiaMorning = Car("KIA Morning", "KIA", "Xanh dương")

# Gọi method drive của object kiaMorning
kiaMorning.drive()


# Tạo object ferrariF8 từ cùng class Car
# Đây là một object KHÁC, dữ liệu KHÁC
ferrariF8 = Car("Ferrari F8", "Ferrari", "Vàng")

# Gọi method drive của object ferrariF8
ferrariF8.drive()
