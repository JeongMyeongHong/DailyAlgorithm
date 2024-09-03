def solution(myString, pat):
    replace_string = ''.join(['A' if i == 'B' else 'B' for i in myString])
    return 1 if pat in replace_string else 0