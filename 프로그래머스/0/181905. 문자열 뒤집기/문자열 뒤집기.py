def solution(my_string, s, e):
    my_string = list(my_string)
    reversed_list = list(reversed(my_string[s:e+1]))
    my_string[s:e+1] = reversed_list
    print(my_string)
    return ''.join(my_string)