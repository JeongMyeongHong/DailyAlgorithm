def solution(code):
    mode = 0
    reg = ''
    for i, c in enumerate(code):
        if c == '1':
            mode ^= 1
            continue
        if (mode == 0) and (i % 2 == 0):
            reg += c
        elif (mode == 1) and (i % 2 == 1):
            reg += c
    return 'EMPTY' if reg == '' else reg