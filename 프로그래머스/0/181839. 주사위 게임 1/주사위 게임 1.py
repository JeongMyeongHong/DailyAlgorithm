def solution(a, b):
    a_rem = a % 2
    b_rem = b % 2
    if a_rem + b_rem == 2:
        return a**2 + b**2
    elif a_rem + b_rem == 0:
        return abs(a - b)
    else:
        return (a + b) * 2
    return answer