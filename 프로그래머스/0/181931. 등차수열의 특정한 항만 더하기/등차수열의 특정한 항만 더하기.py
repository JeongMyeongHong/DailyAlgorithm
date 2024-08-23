def solution(a, d, included):
    answer = 0
    for i, bo in enumerate(included):
        answer = answer + a if bo else answer
        a += d
    return answer