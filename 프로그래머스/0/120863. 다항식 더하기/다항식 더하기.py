def solution(polynomial):
    x_coe = []
    const = []
    polynomial = polynomial.split(' + ')
    for x in polynomial:
        if 'x' in x:
            x_coe.append(int(x[:-1]) if len(x) != 1 else 1)
        else:
            const.append(int(x))
    x_sum = sum([i for i in x_coe])
    const_sum = sum([i for i in const])
    
    result = []
    if x_sum != 0:
        result.append(f'{x_sum}x' if x_sum != 1 else 'x')
    if const_sum != 0:
        result.append(f'{const_sum}')
    
    return ' + '.join(result)