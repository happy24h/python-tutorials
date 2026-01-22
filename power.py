# Hàm tính luỹ thừa
# Ví dụ:
# 2^3 = 8
# 3^3 = 27
def calculate_power(base_number, exponent):
    result = 1
    for index in range(exponent):
        result *= base_number
    return result

print(calculate_power(3, 3))
