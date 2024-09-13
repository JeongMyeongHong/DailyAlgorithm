def solution(s):
    s_dict = {}
    for s in s:
        try:
            s_dict[s] += 1
        except:
            s_dict[s] = 1
    return ''.join(sorted([k for k, v in s_dict.items() if v == 1]))