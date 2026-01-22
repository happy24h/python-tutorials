phone_book = open("phone_book.txt", "r")
# print(phone_book.read())
# print(phone_book.readline())
for person in phone_book.readlines():
    person = person.replace("\n", "")
    print(person)
phone_book.close()