def solution(poly):
    poly = poly.split(' + ')
    x_sum = 0
    n_sum = 0

    for p in poly:
        if p == 'x':
            x_sum += 1
        elif 'x' in p:
            x_sum += int(p.strip('x'))
        else:
            n_sum += int(p)

    if x_sum == 0:
        return str(n_sum)
    elif n_sum == 0:
        if x_sum == 1:
            return 'x'
        else:
            return str(x_sum) + 'x'
    else:
        if x_sum == 1:
            return 'x' + ' + ' + str(n_sum)
        else:
            return str(x_sum) + 'x' + ' + ' + str(n_sum)
