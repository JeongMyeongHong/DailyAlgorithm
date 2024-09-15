def solution(order):
    cnt = 0 
    for i in str(order):
        if int(i) % 3 == 0 and int(i) != 0:
            cnt += 1
    return cnt