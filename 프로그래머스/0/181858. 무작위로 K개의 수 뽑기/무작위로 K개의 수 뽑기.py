def solution(arr, k):
    res = []
    for i in arr:
        if i not in res:
            res.append(i)
            if len(res) == k:
                return res
    res.extend([-1]*(k - len(res)))
    return res