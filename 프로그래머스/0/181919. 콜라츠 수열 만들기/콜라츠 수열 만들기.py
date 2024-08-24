def colats(n, arr):
    arr.append(n)
    if (n % 2) == 0:
        n = n / 2
    else:
        n = 3 * n + 1
    if n == 1:
        return arr.append(n)
    colats(n, arr)
    return arr

def solution(n):
    arr = []
    return colats(n, arr)