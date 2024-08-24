def solution(arr):
    stk = [arr[0]]
    for a in arr[1:]:
        while 1:
            if len(stk)==0:
                stk.append(a)
                break
            if stk[-1] < a:
                stk.append(a)
                break
            else:
                stk = stk[:-1]
    return stk