import re

def extract_numbers(string):
    return re.sub(r'\D', '/', string).split('/')

def solution(my_string):
    answer = 0
    res = extract_numbers(my_string)
    res = [int(i) for i in res if i]
    return sum(res)