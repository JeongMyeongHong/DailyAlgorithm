def solution(before, after):
    a_ls = list(after)
    for b in before:
        if b in a_ls:
            a_ls.remove(b)
        else:
            return 0
    return 1