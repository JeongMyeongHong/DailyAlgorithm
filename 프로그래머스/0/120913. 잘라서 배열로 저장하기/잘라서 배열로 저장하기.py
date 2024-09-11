def solution(my_str, n):
    my_str = list(my_str)
    cut_line = (len(my_str) // n + 1 if len(my_str) % n != 0 else len(my_str) // n)*n
    return [''.join(my_str[i:i+n]) if i != cut_line else ''.join(my_str[i:]) for i in range(0, cut_line, n)]