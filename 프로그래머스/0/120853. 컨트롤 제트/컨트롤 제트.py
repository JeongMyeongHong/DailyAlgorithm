def solution(s):
    answer = 0
    s_ls = s.split(" ")
    for i in range(len(s_ls)):
        if s_ls[i] == "Z":
            answer -= int(s_ls[i-1])
        else:
            answer += int(s_ls[i])
    return answer