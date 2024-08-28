def solution(my_string):
    res = [0 for i in range(52)]
    for my_chr in my_string:
        idx = ord(my_chr)
        if idx > 96:
            idx = idx - 97 + 26
            res[idx] += 1
        else:
            idx = idx - 65
            res[idx] += 1
    return res