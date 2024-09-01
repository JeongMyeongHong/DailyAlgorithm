def solution(myString, pat):
    count = 0
    index = -1
    while 1:
        myString = myString[index+1:]
        try:
            index = myString.index(pat)
        except:
            return count
        count += 1
