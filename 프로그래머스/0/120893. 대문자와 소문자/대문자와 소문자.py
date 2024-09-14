def solution(my_string):
    answer = ''.join([i.upper() if ord(i) > 90 else i.lower() for i in list(my_string)])
    return answer