# Exception (Ngoại lệ)
# Throw an exception (Ném ra một ngoại lệ)
# Handle exception (Xử lý ngoại lệ)
try:
    num1 = int(input("Nhập vào từ số: "))
    num2 = int(input("Nhập vào mẫu số: "))
    result = num1 / num2
    print("Mẫu số phải khác 0. Vui lòng nhập lại!")
except ZeroDivisionError:
    print("Mẫu số phải khác 0. Vui lòng nhập lại")
except ValueError:
    print("Dữ liệu đầu vào phải là các số nguyên. Vui lòng nhập lại")
except:
    print("Có lỗi xảy ra, vui lòng liên hệ trung tâm tư vấn để được hỗ trợ.")
