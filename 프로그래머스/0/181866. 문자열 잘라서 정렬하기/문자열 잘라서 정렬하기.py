def solution(myString):
    ls = [i for i in myString.split('x') if i]
    ls.sort()
    return ls