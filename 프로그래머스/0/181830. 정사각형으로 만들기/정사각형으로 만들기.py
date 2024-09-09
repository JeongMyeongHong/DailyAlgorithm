def solution(arr):
    len_col = len(arr[0])
    len_row = len(arr)
    if len_col == len_row:
        return arr
    elif len_col > len_row:
        len_dif = len_col - len_row
        for _ in range(len_dif):
            arr.append([0]*len_col)
        return arr
    elif len_col < len_row:
        len_dif = len_row - len_col
        for ls in arr:
            ls.extend([0 for _ in range(len_dif)])
        return arr
