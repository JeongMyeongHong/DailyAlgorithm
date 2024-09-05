def solution(arr, n):
    length = len(arr) % 2
    for i in range(1^length, len(arr), 2):
        arr[i] = arr[i] + n
    return arr