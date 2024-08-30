def solution(str_list):
    if 'l' not in str_list and 'r' not in str_list:
        return []
    else:
        for i, s in enumerate(str_list):
            if s == 'l':
                return str_list[:i] if i != 0 else []
            elif s == 'r':
                return str_list[i+1:] if i != len(str_list)-1 else []