# num1 = input("Nhập số thứ nhất: ")
# num2 = input("Nhập số thứ hai: ")
# sum = float(num1) + float(num2)
# print(sum)
num1 = float(input("Nhập số thứ nhất: "))
operator = input("Nhập vào toán tử: ")
num2 = float(input("Nhập số thứ hai: "))
if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
else:
    print("Toán từ không hợp lệ!!!")