import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

import heapq

# 정점의 개수 n, 간선의 개수 m
n, m = map(int, input().split())

# 무한을 의미하는 INF
INF = int(1e9)

# 그래프 초기화
graph = [[] * (n+1) for _ in range(n+1)]

# 간선 정보 입력
for _ in range(m):
    a, b, c = map(int, input().split())
    # a->b가 c비용
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

def dijkstra(start):
    # 최단 거리 테이블을 모두 무한으로 초기화
    distance = [INF] * (n + 1)
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance

# 다익스트라 알고리즘을 수행
one = dijkstra(1)
v1_ = dijkstra(v1)
v2_ = dijkstra(v2)

count = min(one[v1] + v1_[v2] + v2_[n], one[v2] + v2_[v1] + v1_[n])
if count >= INF:
    print(-1)
else:
    print(count)