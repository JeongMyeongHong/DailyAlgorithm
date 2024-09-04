def solution(arr):
    b_len = len(bin(len(arr)))-2
    length = 2**b_len
    return arr + [0]*(length-len(arr)) if len(arr) != 2**(b_len-1) else arr