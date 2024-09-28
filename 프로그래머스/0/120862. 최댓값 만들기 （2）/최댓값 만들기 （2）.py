def solution(numbers):
    sorted_numbers = sorted(numbers, reverse=True)
    max_positive = sorted_numbers[0] * sorted_numbers[1]
    max_negative = sorted_numbers[-1] * sorted_numbers[-2]
    return max(max_positive, max_negative)