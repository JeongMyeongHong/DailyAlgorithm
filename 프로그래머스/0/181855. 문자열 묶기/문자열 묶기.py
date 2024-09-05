def solution(strArr):
    ls = [0]*len(strArr)
    for my_str in strArr:
        ls[len(my_str)] += 1
    return max(ls)