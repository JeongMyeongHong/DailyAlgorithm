def solution(a, b, c, d):
    ls = [a, b, c, d]
    ls.sort()
    ls_set = set(ls)
    if len(ls_set) == 1:
        return 1111 * a
    elif len(ls_set) == 2:
        p = ls[2]
        q = ls[0] if ls[0] != ls[2] else ls[3]
        return (10 * p + q) ** 2 if (p == ls[1]) else (p + q) * (p - q)
    elif len(ls_set) == 3:
        for i in range(0, len(ls)):
            if (ls[i]==ls[i+1]):
                return ls[2]*ls[3] if i == 0 else ls[0] * ls[3] if i == 1 else ls [0] * ls [1]
    else:
        return ls[0]