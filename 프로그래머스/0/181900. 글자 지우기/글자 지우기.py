def solution(my_string, indices):
    indices.sort()
    indices.reverse()
    
    my_string = list(my_string)
    for idx in indices:
        my_string = my_string[:idx] + my_string[idx+1:]
    return ''.join(my_string)