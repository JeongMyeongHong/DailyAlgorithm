def solution(myString):
    answer = []
    for i in list(myString):
        if i == 'a' or i == 'A':
            answer.append('A')
        else:
            answer.append(i.lower())
    return ''.join(answer)