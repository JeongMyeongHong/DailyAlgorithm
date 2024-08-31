def div(num):
    cnt = 0
    while 1:
        if num == 1:
            return cnt
        elif num % 2 == 0:
            num = int(num / 2)
        elif num % 2 != 0:
            num = int((num - 1) / 2)
        cnt += 1
            
def solution(num_list):
    answer = 0
    for i in num_list:
        answer += div(i)
    return answer