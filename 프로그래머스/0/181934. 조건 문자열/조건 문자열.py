def solution(ineq, eq, n, m):
    if (eq == "=" and n == m):
        return 1
    elif (ineq == ">"):
        return 1 if (n > m) else 0
    else:
        return 1 if (n < m) else 0
