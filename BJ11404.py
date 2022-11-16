n = int(input())
m = int(input())
INF = int(1e9)

# 노드간 이동 비용 그래프
dis = [[INF for i in range(n)] for j in range(n)]

# 자기자신으로 가는 경우는 없으므로 비용을 0으로 초기화
for i in range(n):
    dis[i][i] = 0

# 출발점, 도착점, 비용을 입력으로 받아서 dis에 넣어준다
for i in range(m):
    a, b, c = map(int, input().split())
    if dis[a-1][b-1] > c:
        dis[a-1][b-1] = c

# 플로이드 와샬 알고리즘.
for k in range(n):
    for i in range(n):
        for j in range(n):
            # k를 거쳐서 가는 경로와 i에서 바로 j로 가는 경로를 비교하여 비용이 더 작은것으로 dis를 초기화한다.
            dis[i][j] = min(dis[i][k] + dis[k][j], dis[i][j])

for i in range(n):
    for j in range(n):
        #dis의 값이 INF이면 경로가 존재하지 않는것으로 0을 출력
        if dis[i][j] == INF:
            print(0, end=" ")
        else:
            print(dis[i][j], end=" ")
    print()

