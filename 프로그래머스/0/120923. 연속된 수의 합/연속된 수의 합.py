def solution(num, total):
    answer = []
    if num % 2 == 1:
        mid = int(total / num)
        div = num // 2
        return [i - div for i in range(mid, mid + num)]
    else:
        start = int((total / num * 2 ) // 2 - (num / 2 - 1))
        return list(range(start, start + num))
