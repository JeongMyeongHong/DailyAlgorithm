def solution(n_str):
    while 1:
        if n_str[0] == '0':
            n_str = n_str[1:]
        else:
            return n_str
