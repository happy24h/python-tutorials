secret_word = "python"
hint = "Gợi ý: Đây là tên một ngôn ngữ lập trình"
guess = ""
guess_count = 0
guess_limit = 3

print(hint)

while guess != secret_word:
    if guess_count < guess_limit:
        guess = input("Bạn đoán đây là từ gì? ")
        guess_count += 1
    else:
        break

if guess == secret_word:
    print("Bãn đã đoán chính xác!")
else:
    print("Bạn đã thất bại vì đoán sai 3 lần")