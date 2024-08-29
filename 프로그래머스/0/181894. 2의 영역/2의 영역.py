def solution(arr):
    cnt = arr.count(2)
    if cnt == 0:
        return [-1]
    elif cnt == 1:
        return [arr[arr.index(2)]]
    elif cnt > 1:
        idx = arr.index(2)
        r_idx = list(reversed(arr)).index(2)
        return arr[idx:-r_idx] if r_idx != 0 else arr[idx:]