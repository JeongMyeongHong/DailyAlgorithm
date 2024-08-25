import copy

def reverse_function(my_string, query):
    s = query[0]
    e = query[1] + 1
    my_string = list(my_string)
    res = copy.deepcopy(my_string)
    for (idx, i) in enumerate(range(s, e)):
        res[i] = my_string[e - idx - 1]
    return ''.join(res)


def solution(my_string, queries):
    for query in queries:
        my_string = reverse_function(my_string, query)
    return my_string