def solution(rank, attendance):
    answer = 0
    ls = []
    for r, a in zip(rank, attendance):
        if a:
            ls.append(r)
    ls.sort()
    return 10000*rank.index(ls[0]) + 100*rank.index(ls[1]) + rank.index(ls[2])