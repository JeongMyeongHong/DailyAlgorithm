def solution(score):
    avg_list = []
    for student in score:
        avg_list.append(sum(student) / len(student))
    answer = [sorted(avg_list, reverse=True).index(i)+1 for i in avg_list]
    return answer