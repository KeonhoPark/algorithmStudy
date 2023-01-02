import copy
from collections import deque

h, c = map(int, input().split())
q = list()
q = deque(q)
ch_q = list()
ch_q = deque(ch_q)
visited = [0 for i in range(1, 10001)]
count = 0

q.append(h)
while True:
    if len(q) == 0:
        count += 1
        q = copy.deepcopy(ch_q)
    pos = q.popleft()
    visited[pos] = 1
    if pos == c:
        break
    for next_pos in (pos+1, pos+5, pos-1):
        if 0 < next_pos < 10001 and visited[next_pos] == 0:
            visited[next_pos] = 1
            ch_q.append(next_pos)

print(count)




