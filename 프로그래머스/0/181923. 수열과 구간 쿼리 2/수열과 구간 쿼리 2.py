def solution(arr, queries):
    answer = []
    for (s, e, k) in queries:
        ls = list(filter(lambda x: x > k, arr[s:e+1]))
        if len(ls) == 0:
            ls = [-1]
        answer.append(min(ls))
        
    return answer