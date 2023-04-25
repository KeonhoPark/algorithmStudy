from collections import deque


def solution(game_board, table):
    res = 0

    def table_cluster(graph):
        s = len(graph)
        visited = [[0 for _ in range(s)] for _ in range(s)]
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        res_list = list()

        for i in range(s):
            for j in range(s):
                if graph[i][j] == 1 and visited[i][j] == 0:
                    q = deque()
                    cor_list = list()
                    q.append([i, j])
                    cor_list.append([i, j])
                    visited[i][j] = 1
                    while q:
                        cor = q.popleft()
                        y = cor[0]
                        x = cor[1]

                        for k in range(4):
                            new_y = y + dy[k]
                            new_x = x + dx[k]
                            if 0 <= new_y < s and 0 <= new_x < s and graph[new_y][new_x] == 1 and visited[new_y][
                                new_x] == 0:
                                q.append([new_y, new_x])
                                visited[new_y][new_x] = 1
                                cor_list.append([new_y, new_x])

                    res_list.append(cor_list)

        return res_list

    def board_cluster(graph):
        s = len(graph)
        visited = [[0 for _ in range(s)] for _ in range(s)]
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        res_list = list()

        for i in range(s):
            for j in range(s):
                if graph[i][j] == 0 and visited[i][j] == 0:
                    q = deque()
                    cor_list = list()
                    q.append([i, j])
                    cor_list.append([i, j])
                    visited[i][j] = 1
                    while q:
                        cor = q.popleft()
                        y = cor[0]
                        x = cor[1]

                        for k in range(4):
                            new_y = y + dy[k]
                            new_x = x + dx[k]
                            if 0 <= new_y < s and 0 <= new_x < s and graph[new_y][new_x] == 0 and visited[new_y][
                                new_x] == 0:
                                q.append([new_y, new_x])
                                visited[new_y][new_x] = 1
                                cor_list.append([new_y, new_x])

                    res_list.append(cor_list)

        return res_list

    def rotate(graph):
        s = len(graph)
        r_graph = [[] for _ in range(s)]

        for i in range(s):
            tmp = list()
            for j in range(s - 1, -1, -1):
                tmp.append(graph[j][i])
            r_graph[i] = tmp

        return r_graph

    def count(blanks, puzzles):
        count = 0
        filled_blanks = list()

        for b in blanks:
            flag = 0
            sorted_b = sorted(b)
            for p in puzzles[::]:
                sorted_p = sorted(p)
                if len(b) == len(p) and flag == 0:
                    y_diff = sorted_b[0][0] - sorted_p[0][0]
                    x_diff = sorted_b[0][1] - sorted_p[0][1]

                    for i in range(len(sorted_p)):
                        new_cor = [sorted_p[i][0] + y_diff, sorted_p[i][1] + x_diff]
                        if new_cor != sorted_b[i]:
                            break

                    else:
                        count += len(p)
                        puzzles.remove(p)
                        flag = 1
                        if b not in filled_blanks:
                            filled_blanks.append(b)

        return count, filled_blanks, puzzles

    def fill_blanks(board, blanks):

        for b in blanks:
            for cor in b:
                board[cor[0]][cor[1]] = 1

        return board

    puzzles = table_cluster(table)

    for _ in range(4):
        blanks = board_cluster(game_board)
        c, f_b, p = count(blanks, puzzles)
        res += c
        puzzles = p
        game_board = fill_blanks(game_board, f_b)
        game_board = rotate(game_board)

    return res


solution([[1, 1, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0], [0, 1, 1, 0, 0, 1], [1, 1, 0, 1, 1, 1], [1, 0, 0, 0, 1, 0], [0, 1, 1, 1, 0, 0]], [[1, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 0], [0, 0, 1, 0, 1, 1], [0, 1, 1, 0, 0, 0], [1, 1, 0, 1, 1, 0], [0, 1, 0, 0, 0, 0]])
