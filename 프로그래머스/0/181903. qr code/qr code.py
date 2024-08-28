def solution(q, r, code):
    return ''.join([cd if i%q==r else '' for (i, cd) in enumerate(code)])