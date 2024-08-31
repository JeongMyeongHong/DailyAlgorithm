def calc(arr):
    nextArr = []
    for idx, i in enumerate(arr):
        if i >= 50 and i % 2 == 0:
            nextArr.append(int(i / 2))
        elif i < 50 and i % 2 == 1:
            nextArr.append(i * 2 + 1)
    return nextArr

def solution(arr):
    cnt = 0
    nextArr = calc(arr)
    while(1):
        arr = nextArr
        nextArr = calc(arr)
        if nextArr == arr:
            return cnt
        cnt += 1
    