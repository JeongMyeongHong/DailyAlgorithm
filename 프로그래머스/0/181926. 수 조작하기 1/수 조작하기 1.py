def solution(n, control):
    control = control.replace("w", "+1").replace("s", "-1").replace("d", "+10").replace("a", "-10")
    return eval(str(n)+control)