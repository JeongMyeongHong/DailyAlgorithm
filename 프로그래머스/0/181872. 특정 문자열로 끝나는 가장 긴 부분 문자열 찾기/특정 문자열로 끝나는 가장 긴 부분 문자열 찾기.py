def solution(myString, pat):
    answer = ''
    myString_copy = list(myString)
    myString_copy.reverse()
    myString_copy = ''.join(myString_copy)
    pat = list(pat)
    pat.reverse()
    pat = ''.join(pat)
    
    index = myString_copy.index(pat)
    
    return myString[:-index] if index != 0 else myString