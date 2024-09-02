def solution(myString):
    ls = myString.split('x')
    return [len(i) for i in ls]