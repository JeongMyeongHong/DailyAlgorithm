def solution(array):
    cnt = 0
    for arr in array:
        arr = list(str(arr))
        for e in arr:
            if e == '7':
                cnt += 1
    return cnt