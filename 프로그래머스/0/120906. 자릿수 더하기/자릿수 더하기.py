def solution(n):
    sum = 0
    for i in list(str(n)):
        sum += int(i)
    return sum