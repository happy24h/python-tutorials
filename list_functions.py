student_names = ["Nguyên", "Hưng", "Tuyên", "Trung", "Sáng", "Trường"]
math_scores = [10, 9, 8, 7, 6, 5, 4]
print(math_scores)
print(student_names)
student_names.append("Thắng") # thêm phần tử ở cuối mảng
student_names.insert(3, "Thu") # thêm tên ở vị trí số 3
student_names.remove("Sáng") # xoá tên Sáng
# student_names.clear() # xoá hết phần tử trong mảng
# student_names.pop() # xoá phần tử cuối cùng
print(student_names.index("Tuyên")) # tìm phần tử trong danh sách
print(student_names.count("Nguyên")) # đếm xem có mấy giá trị này
print(math_scores.sort()) # Sắp xếp theo thứ tu tăng dần
print(math_scores.reverse()) # Đảo ngược thứ tự
print(math_scores)

# student_names.extend(math_scores) # nối 2 danh sách lại với nhau
print(student_names)

student_names_2 = student_names.copy() #Copy mảng student_names
print(student_names_2)