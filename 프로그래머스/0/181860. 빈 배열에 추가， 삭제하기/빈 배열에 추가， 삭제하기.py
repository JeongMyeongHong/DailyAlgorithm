def solution(arr_list, flags):
    answer = []
    for arr, flag in zip(arr_list, flags):
        if flag:
            answer.extend([arr]*arr*2)
        else:
            answer = answer[:-arr]
    return answer