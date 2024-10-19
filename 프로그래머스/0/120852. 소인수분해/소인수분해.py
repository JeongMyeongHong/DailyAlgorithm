def solution(n):
    answer = set()
    div = 2
    while n != 1:
        if n % div == 0:
            n /= div
            answer.add(div)
        else:
            div += 1
    return sorted(list(answer))