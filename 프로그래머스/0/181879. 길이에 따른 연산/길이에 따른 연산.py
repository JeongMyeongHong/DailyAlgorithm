def mul(ls):
    res = 1
    for i in ls:
        res *= i
    return res

def solution(num_list):
    return sum(num_list) if len(num_list) >= 11 else mul(num_list)