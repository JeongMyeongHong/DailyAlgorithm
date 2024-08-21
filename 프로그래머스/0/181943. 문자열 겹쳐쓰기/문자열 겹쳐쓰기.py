def solution(my_string, overwrite_string, s):
    answer = my_string[:s] + overwrite_string
    if (len(my_string)> len(overwrite_string) + s):
        answer = answer + my_string[len(overwrite_string) + s:]
    return answer