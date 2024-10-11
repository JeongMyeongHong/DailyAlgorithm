def solution(dots):
    line1 = []
    for i in range(1, 4):
        dots_copy = dots.copy()
        line1.append(dots_copy.pop(i))
        line1.append(dots_copy.pop(0))
        line2 = dots_copy
        
        incline1 = (line1[1][1]-line1[0][1])/(line1[1][0]-line1[0][0])
        incline2 = (line2[1][1]-line2[0][1])/(line2[1][0]-line2[0][0])
        
        if incline1 == incline2:
            return 1
        line1.clear()
    return 0