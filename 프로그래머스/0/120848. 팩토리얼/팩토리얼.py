def solution(n):
    num = 1
    while(n>=1):
        n /= num
        num += 1
    return num -2