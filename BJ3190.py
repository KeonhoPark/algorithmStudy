n = int(input())
k = int(input())
board = [[0 for _ in range(n)] for _ in range(n)]
board[0][0] = 's'

#방향전환을 담기위한 리스트
directions = [0 for _ in range(10001)]

#방향전환이 일어난 좌표
dir_change = [[0 for _ in range(n)] for _ in range(n)]

#사과의 위치를 받아 board에 a로 저장
for i in range(k):
    r, c = map(int, input().split())
    board[r - 1][c - 1] = 'a'

# 방향 변환 횟수 받음
l = int(input())

#directions 리스트에 인덱스(초)에 해당하는 회전방향 삽입
for i in range(l):
    t, d = (input().split())
    directions[int(t)] = d


#board를 벗어남을 검사하는 함수
#진행할 방향과 머리의 좌표를 받아 방향으로 진행할때 뱀이 벽과 부딪히게 되는지 검사해준다.
def is_out(dir, h_row, h_col):
    if dir == 'u':
        if h_row - 1 < 0:
            return True
        else:
            return False
    elif dir == 'l':
        if h_col - 1 < 0:
            return True
        else:
            return False
    elif dir == 'r':
        if h_col + 1 > n - 1:
            return True
        else:
            return False
    elif dir == 'd':
        if h_row + 1 > n - 1:
            return True
        else:
            return False

#뱀이 단순히 움직일때(사과를 먹지않고) 다음 꼬리가되는 부분의 좌표를 돌려주는 함수
#dir_change 이차원 리스트에 있는 뱡향정보를 가지고 다음 꼬리의 좌표를 계산하여 리턴.
def change_tail(t_row, t_col):
    if dir_change[t_row][t_col] == 'u':
        return t_row-1, t_col
    elif dir_change[t_row][t_col] == 'l':
        return t_row, t_col-1
    elif dir_change[t_row][t_col] == 'r':
        return t_row, t_col+1
    elif dir_change[t_row][t_col] == 'd':
        return t_row+1, t_col

# 뱀의 움직임을 구현한 함수
# 이동할 방향과 머리 좌표, 꼬리 좌표를 받는다.
# 이동할 방향대로 움직인 후의 머리 좌표, 꼬리 좌표를 리턴.
def move(dir, h_row, h_col, t_row, t_col):

    #is_out() 함수를 사용하여 다음방향으로 이동할때 벽에 부딪히면 머리좌표와 꼬리좌표를 각각 (-1, -1)로 리턴
    if is_out(dir, h_row, h_col):
        return -1, -1, -1, -1

    # 각각의 방향(u, l, r, d)에 따라 사과를 먹었을 때, 자신의 몸을 만났을때, 사과를 먹지 않았을때로 나뉨
    else:
        # 이동할 방향이 위이면
        if dir == 'u':
            # 머리의 윗방향에 사과가 있으면 사과를 뱀으로 바꿔주고 꼬리의 위치는 변하지 않는다.
            if board[h_row - 1][h_col] == 'a':
                board[h_row - 1][h_col] = 's'
                # 변한 머리좌표를 반환해주고 꼬리좌표는 바뀌지 않았으니 그대로 리턴.
                return h_row-1, h_col, t_row, t_col
            # 머리의 윗방향에 뱀이 있으면 머리좌표와 꼬리좌표를 각각 (-1, -1)로 리턴.
            elif board[h_row - 1][h_col] == 's':
                return -1, -1, -1, -1

            # 머리의 윗방향에 아무것도 없으면 위의 좌표에 뱀을 넣어주고 꼬리좌표에는 0을 넣어준다.
            else:
                board[h_row - 1][h_col] = 's'
                board[t_row][t_col] = 0
                # change_tail() 함수를 이용하여 바뀐 꼬리좌표를 받아준다.
                new_t_row, new_t_col = change_tail(t_row, t_col)
                # 바뀐 머리좌표와 꼬리좌표를 리턴.
                return h_row-1, h_col, new_t_row, new_t_col

        elif dir == 'l':
            if board[h_row][h_col - 1] == 'a':
                board[h_row][h_col - 1] = 's'
                return h_row, h_col-1, t_row, t_col
            elif board[h_row][h_col - 1] == 's':
                return -1, -1, -1, -1
            else:
                board[h_row][h_col - 1] = 's'
                board[t_row][t_col] = 0
                new_t_row, new_t_col = change_tail(t_row, t_col)
                return h_row, h_col-1, new_t_row, new_t_col

        elif dir == 'r':
            if board[h_row][h_col + 1] == 'a':
                board[h_row][h_col + 1] = 's'
                return h_row, h_col+1, t_row, t_col
            elif board[h_row][h_col + 1] == 's':
                return -1, -1, -1, -1
            else:
                board[h_row][h_col + 1] = 's'
                board[t_row][t_col] = 0
                new_t_row, new_t_col = change_tail(t_row, t_col)
                return h_row, h_col+1, new_t_row, new_t_col

        elif dir == 'd':
            if board[h_row + 1][h_col] == 'a':
                board[h_row + 1][h_col] = 's'
                return h_row+1, h_col, t_row, t_col
            elif board[h_row + 1][h_col] == 's':
                return -1, -1, -1, -1
            else:
                board[h_row + 1][h_col] = 's'
                board[t_row][t_col] = 0
                new_t_row, new_t_col = change_tail(t_row, t_col)
                return h_row+1, h_col, new_t_row, new_t_col

#방향을 바꿔주는 함수
#현재 방향과 시간, 머리좌표를 받는다.
def change_dir(curr_dir, time, h_row, h_col):
    #directions 리스트에 time 인덱스에 해당하는 값이 0이면 방향전환이 없는것이므로 현재방향 그대로 리턴
    if directions[time] == 0:
        # 머리의 좌표에 현재 방향을 찍는다.
        dir_change[h_row][h_col] = curr_dir
        return curr_dir
    elif curr_dir == 'u' and directions[time] == 'L':
        # 머리의 좌표에 바뀐 방향을 찍는다. 이렇게되면 어느좌표에서 방향전환이 일어났는지 알수있음
        dir_change[h_row][h_col] = 'l'
        return 'l'
    elif curr_dir == 'u' and directions[time] == 'D':
        dir_change[h_row][h_col] = 'r'
        return 'r'
    elif curr_dir == 'l' and directions[time] == 'L':
        dir_change[h_row][h_col] = 'd'
        return 'd'
    elif curr_dir == 'l' and directions[time] == 'D':
        dir_change[h_row][h_col] = 'u'
        return 'u'
    elif curr_dir == 'r' and directions[time] == 'L':
        dir_change[h_row][h_col] = 'u'
        return 'u'
    elif curr_dir == 'r' and directions[time] == 'D':
        dir_change[h_row][h_col] = 'd'
        return 'd'
    elif curr_dir == 'd' and directions[time] == 'L':
        dir_change[h_row][h_col] = 'r'
        return 'r'
    elif curr_dir == 'd' and directions[time] == 'D':
        dir_change[h_row][h_col] = 'l'
        return 'l'


t = 0
#시작시 방향은 오른쪽이므로 curr_dir을 'r'로 초기화
curr_dir = 'r'
#꼬리의 방향도 오른쪽으로 초기화
t_curr_dir = 'r'

#머리좌표와 꼬리좌표 각각 (0, 0)으로 초기화
h_row = 0
h_col = 0
t_row = 0
t_col = 0
while True:
    #방향 바꿔줌. 바뀌는 시점이 아니라면 기존 방향 그대로 리턴.
    curr_dir = change_dir(curr_dir, t, h_row, h_col)

    #다음 머리좌표와 꼬리좌표가 나옴
    h_row, h_col, t_row, t_col = move(curr_dir, h_row, h_col, t_row, t_col)

    #머리가 (-1, -1)이면 벽에 박았거나 자신의 몸에 박았으므로 시간에 + 1 해주고 break
    if h_row == -1 and h_col == -1:
        t += 1
        break
    else:
        t += 1

print(t)




