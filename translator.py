# Ứng Dụng Chuyển Đổi Ngôn Ngữ
# Biến đổi các chữ cái có dấu thành không dấu
# Ví dụ:
# "Trần Minh Sáng" ---> "Tran Minh Sang"
# "Sáng Và Ngân" ---> "Sang Va Ngan"

def translate(text):
    translation = ""
    for character in text:
        if character.lower() in "áàảãạăắằẳẵặâấầẩẫậ":
            if character.isupper():
                translation = translation + "A"
            else:
                translation = translation + "a"
        else:
            translation = translation + character
    return translation

text = input("Nhập vào văn bản mà bạn muốn giao dịch: ")
print(translate(text))
