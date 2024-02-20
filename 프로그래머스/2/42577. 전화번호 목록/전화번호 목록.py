def solution(phone_book):
    answer = True
    s = set(phone_book)

    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in s and temp != phone_number:
                answer = False
    return answer