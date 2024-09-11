def solution(quiz):
    answer = []
    for q in quiz:
        question = q.split("=")
        if eval(question[0]) == int(question[1]):
            answer.append("O")
        else:
            answer.append("X")
    return answer