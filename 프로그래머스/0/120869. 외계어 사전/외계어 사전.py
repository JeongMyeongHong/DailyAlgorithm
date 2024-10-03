def solution(spell, dic):
    for word in dic:
        word_ls = list(word)
        if len(word_ls) == len(spell):
            for sp in spell:
                if sp in word_ls:
                    word_ls.remove(sp)
                else:
                    break
            print(word_ls)
            if len(word_ls) == 0:
                return 1
    return 2