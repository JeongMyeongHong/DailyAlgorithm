def solution(picture, k):
    answer = []
    for pic in picture:
        pic_k = ''.join([p * k for p in pic])
        answer.extend([pic_k] * k)
    return answer