def solution(array, n):
    array.sort()
    dif_arr = [abs(i - n) for i in array]
    return array[dif_arr.index(min(dif_arr))]