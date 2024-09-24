def solution(chicken):
    if chicken == 0 :
        return 0
    return chicken // 9 if chicken % 9 != 0 else chicken // 9 - 1