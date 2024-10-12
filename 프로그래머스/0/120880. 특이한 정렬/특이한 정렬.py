def solution(numlist, n):
    answer = []
    num_dict = dict()
    for num in numlist:
        num_dict[num] = abs(n-num)
    sort_abs_list = sorted(set([abs(n-i) for i in numlist]))
    for e in sort_abs_list:
        keys = [k for k, v in num_dict.items() if v == e]
        if len(keys) == 1:
            answer.append(keys[0])
        else:
            keys.sort()
            answer.append(keys[1])
            answer.append(keys[0])
    return answer