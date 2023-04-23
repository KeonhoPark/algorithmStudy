from collections import deque


def solution(game_board, table):
    blank = list()
    blank_dir = list()
    puzzle = list()
    puzzle_dir = list()

    def cluster(matrix, flag, t):

        e = 0
        if t == 0:
            e = 1

        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        directions = ['d', 'r', 'u', 'l']

        row = len(matrix[0])
        col = len(matrix)

        for i in range(col):
            for j in range(row):
                if matrix[i][j] == t:
                    dir_list = list()
                    q = deque()
                    q.append([i, j])
                    dir_list.append([i, j])
                    matrix[i][j] = e

                    while q:
                        cor = q.popleft()
                        y = cor[0]
                        x = cor[1]

                        for k in range(4):
                            new_y = y + dy[k]
                            new_x = x + dx[k]

                            if 0 <= new_y < col and 0 <= new_x < row and matrix[new_y][new_x] == t:
                                q.append([new_y, new_x])
                                dir_list.append([new_y, new_x, directions[k]])
                                matrix[new_y][new_x] = e

                    if flag == 0:
                        blank.append(dir_list)
                    else:
                        puzzle.append(dir_list)

    def get_dir(points):
        dir_list = list()

        for p in points:
            d = list()
            tmp = points.copy()
            tmp.remove(p)
            visited = [0 for _ in range(len(tmp))]

            q = deque()
            q.append(p)

            while q:
                cor = q.popleft()
                y = cor[0]
                x = cor[1]
                for i in range(len(tmp)):
                    if visited[i] == 0 and y == tmp[i][0] - 1 and x == tmp[i][1]:
                        d.append('d')
                        q.append([tmp[i][0], tmp[i][1]])
                        visited[i] = 1
                    elif visited[i] == 0 and y == tmp[i][0] and x == tmp[i][1] - 1:
                        d.append('r')
                        q.append([tmp[i][0], tmp[i][1]])
                        visited[i] = 1
                    elif visited[i] == 0 and y == tmp[i][0] + 1 and x == tmp[i][1]:
                        d.append('u')
                        q.append([tmp[i][0], tmp[i][1]])
                        visited[i] = 1
                    elif visited[i] == 0 and y == tmp[i][0] and x == tmp[i][1] + 1:
                        d.append('l')
                        q.append([tmp[i][0], tmp[i][1]])
                        visited[i] = 1

            d.sort()
            dir_list.append(d)
            dir_list.sort()

        return dir_list

    def right(direction_list):
        for directions in direction_list:
            for i in range(len(directions)):
                if directions[i] == 'd':
                    directions[i] = 'l'
                elif directions[i] == 'l':
                    directions[i] = 'u'
                elif directions[i] == 'u':
                    directions[i] = 'r'
                else:
                    directions[i] = 'd'

            directions.sort()

        direction_list.sort()

    def count(blank_dir, puzzle_dir):
        count = 0

        for p in puzzle_dir:
            if p in blank_dir:
                # print("1", p)
                # print(blank_dir.index(p))
                count += (len(p[0]) + 1)
                blank_dir.pop(blank_dir.index(p))
            else:
                for i in range(3):
                    right(p)
                    # print("r", p)
                    if p in blank_dir:
                        # print("=", p)
                        # print(blank_dir.index(p))
                        count += (len(p[0]) + 1)
                        blank_dir.pop(blank_dir.index(p))
                        break

        return count

    # for g in game_board:
    #     print(g)
    # print()
    # for t in table:
    #     print(t)
    cluster(game_board, 0, 0)
    cluster(table, 1, 1)
    for p in puzzle:
        puzzle_dir.append(get_dir(p))
    for b in blank:
        blank_dir.append(get_dir(b))

    # print("blank")
    # for i in range(len(blank_dir)):
    #     print(blank_dir[i])

    #     print("puzzle_dir")
    #     for i in range(len(puzzle_dir)):
    #         print(puzzle_dir[i])

    #     print()
    # print(count(blank_dir, puzzle_dir))
    return count(blank_dir, puzzle_dir)

solution([[1, 1, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0], [0, 1, 1, 0, 0, 1], [1, 1, 0, 1, 1, 1], [1, 0, 0, 0, 1, 0], [0, 1, 1, 1, 0, 0]], [[1, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 0], [0, 0, 1, 0, 1, 1], [0, 1, 1, 0, 0, 0], [1, 1, 0, 1, 1, 0], [0, 1, 0, 0, 0, 0]])
#solution([[0, 0, 0], [1, 1, 0], [1, 1, 1]], [[1, 1, 1], [1, 0, 0], [0, 0, 0]])