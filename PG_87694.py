from collections import deque


def solution(rectangle, character_x, character_y, item_x, item_y):
    def is_in(p_y, p_x, rect):
        ld_x = rect[0] * 2
        ld_y = rect[1] * 2
        ru_x = rect[2] * 2
        ru_y = rect[3] * 2

        if ld_y < p_y < ru_y and ld_x < p_x < ru_x:
            return True

        return False

    def in_rectangle(y, x):

        for re in rectangle:
            if is_in(y, x, re):
                return True

        return False

    graph = [[0 for _ in range(102)] for _ in range(102)]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    for r in rectangle:
        ld_x = r[0] * 2
        ld_y = r[1] * 2
        ru_x = r[2] * 2
        ru_y = r[3] * 2

        for i in range(ld_y, ru_y + 1):
            for j in range(ld_x, ru_x + 1):
                graph[i][j] = 1

    character_y *= 2
    character_x *= 2
    item_y *= 2
    item_x *= 2

    q = deque()
    q.append([character_y, character_x, 1])
    graph[character_y][character_x] = 2

    while q:
        cor = q.popleft()
        y = cor[0]
        x = cor[1]
        count = cor[2]
        graph[y][x] = count

        if y == item_y and x == item_x:
            return (count - 1) // 2

        for l in range(4):
            new_y = y + dy[l]
            new_x = x + dx[l]

            if graph[new_y][new_x] == 1 and not in_rectangle(new_y, new_x):
                q.append([new_y, new_x, count + 1])
                graph[new_y][new_x] = 2


print(solution([[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]], 1, 3, 7, 8))
