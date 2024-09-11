def solution(A, B):
    B = list(B)
    cnt = 0
    for i in range(len(A)):
        if list(A) == (B[i:]+B[:i]):
            return cnt
        cnt += 1
    return -1