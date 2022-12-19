from collections import deque

t = int(input())
for i in range(t):
    n, index = map(int, input().split())
    priority = list(map(int, input().split()))
    priority = deque(priority)
    count = 0
    while len(priority) != 0:
        max_p = max(priority)
        if priority[0] == max_p and index == 0:
            priority.popleft()
            count += 1
            break
        elif priority[0] == max_p:
            priority.popleft()
            count += 1
            index -= 1
        elif priority[0] < max_p and index == 0:
            priority.append(priority.popleft())
            index = len(priority) - 1
        elif priority[0] < max_p:
            priority.append(priority.popleft())
            index -= 1
    print(count)
