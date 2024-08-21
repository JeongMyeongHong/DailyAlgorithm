def solution(a, b):
    f = int(str(a)+str(b))
    b = int(str(b)+str(a))
    return f if f > b else b