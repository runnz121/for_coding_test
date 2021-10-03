# def solution(phone_book):
#     answer = True
#     phone_book.sort()
#
#     for i in range(len(phone_book)-1):
#         length = len(phone_book[i])
#         if phone_book[i] == phone_book[i+1][:length]:
#             answer = False
#             break
#     return answer


def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        print(phoneBook[1:])
        if p2.startswith(p1):
            return False
    return True


phone_book = ["119", "97674223", "1195524421"]
phone_book1 = ["123", "456", "789"]
phone_book2 = ["119","119"]
phone_book3 = ["934793", "34", "44", "9347"]
solution(phone_book)