def solution(board, k):
    answer = 0
    for i in range(len(board)):
        if i > k:
            return answer
        for j in range(len(board[i])):
            answer += board[i][j]
            if i + j == k:
                break
    return answer