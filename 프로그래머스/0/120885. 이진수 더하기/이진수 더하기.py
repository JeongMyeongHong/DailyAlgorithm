def solution(bin1, bin2):
    if len(bin1) < len(bin2):
        ls2 = list(bin1)
        ls1 = list(bin2)
    else:
        ls1 = list(bin1)
        ls2 = list(bin2)
    len_dif = len(ls1)-len(ls2)
    ls2 = [0]*len_dif + ls2
    plus = 0
    res = []
    for i in range(len(ls1)-1, -1, -1):
        num = int(ls1[i]) + int(ls2[i]) + plus
        if num >= 2:
            plus = 1
            num = num - 2
        else:
            plus = 0
        res.append(str(num))
    if plus == 1:
        res.append('1')
    res.reverse()
    return ''.join(res)
