def solution(myStr):
    myStr = myStr.replace('b', 'a').replace('c', 'a')
    myStr = [i for i in myStr.split('a') if i != '']
    return myStr if len(myStr) != 0 else ["EMPTY"]