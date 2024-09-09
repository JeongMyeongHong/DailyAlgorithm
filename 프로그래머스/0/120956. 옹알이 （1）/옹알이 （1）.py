def solution(babbling):
    words = ["aya", "ye", "woo", "ma"]
    answer = 0
    for bab in babbling:
        cnt = 0
        for word in words:
            if word in bab:
                bab = bab.replace(word, '/')
                cnt += 1
            if bab == '/'*cnt:
                answer += 1
                break
    return answer