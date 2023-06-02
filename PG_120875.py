import copy


def solution(dots):
    def get_dx_dy(p1, p2):
        x1 = p1[0]
        y1 = p1[1]
        x2 = p2[0]
        y2 = p2[1]

        return abs(x1 - x2), abs(y1 - y2)

    def is_parallel(dx1, dy1, dx2, dy2):
        if (dy1 / dx1) == (dy2 / dx2):
            return True
        else:
            return False

    for i in range(len(dots) - 1):
        for j in range(i + 1, len(dots)):
            tmp = copy.deepcopy(dots)
            tmp.remove(dots[i])
            tmp.remove(dots[j])
            dx1, dy1 = get_dx_dy(dots[i], dots[j])
            dx2, dy2 = get_dx_dy(tmp[0], tmp[1])
            if is_parallel(dx1, dy1, dx2, dy2):
                return 1

    return 0
