def solution(number, n, m):
    return (1 if number % n == 0 else 0) * (1 if number % m == 0 else 0)