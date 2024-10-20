def solution(numbers):
    max_1 = max(numbers)
    numbers.remove(max_1)
    max_2 = max(numbers)
    numbers.remove(max_2)
    return max_1*max_2