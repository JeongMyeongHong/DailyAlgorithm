def solution(my_strings, parts):
    return ''.join([my_string[parts[idx][0]:parts[idx][1]+1] for (idx, my_string) in enumerate(my_strings)])