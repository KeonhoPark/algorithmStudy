from collections import deque

n, m, v = map(int, input().split())

#인접행렬 생성, 각 노드간 연결상태를 저장
matrix = [[0] * (n + 1) for i in range(n + 1)]

#dfs 방문노드 저장 리스트
visited_dfs = [0] * (n + 1)

#bfs 방문노드 저장 리스트
visited_bfs = [0] * (n + 1)

#인접행렬에 노드연결상태를 저장한다. 노드들끼리 연결되어있으면 1을 저장한다.
for i in range(m):
    a, b = map(int, input().split())
    #양방향 간선
    matrix[a][b] = matrix[b][a] = 1

def dfs(v):
    visited_dfs[v] = 1
    print(v, end=' ')
    for i in range(1, 1 + n):
        #루트노드 다음으로 아직 방문을 안했고 루트노드와 연결되어있는 노드들부터 방문한다.
        #재귀법을 사용하여 dfs 구현
        if visited_dfs[i] == 0 and matrix[v][i] == 1:
            dfs(i)

def bfs(v):
    #bfs에는 큐를 사용. 빠른 속도를 위해 deque를 사용한다. 처음에 루트노드를 큐에 저장
    queue = deque([v])
    #루트노드를 방문완료로 설정
    visited_bfs[v] = 1

    #큐가 빌때까지
    while queue:
        #우선 루트노드를 큐에서 뺀다.
        v = queue.popleft()
        print(v, end=' ')
        for i in range(1, 1 + n):
            #dfs와 마찬가지로 아직 방문을 안했고 루트노드와 연결이 되어있는 노드들을 큐에 넣는다.
            if(visited_bfs[i] == 0 and matrix[v][i] == 1):
                queue.append(i)
                visited_bfs[i] = 1

dfs(v)
print()
bfs(v)

