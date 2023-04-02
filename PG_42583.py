from collections import deque


def solution(bridge_length, weight, trucks):
    time = 1
    bridge = deque([0 for _ in range(bridge_length)])
    bridge[-1] = trucks[0]
    trucks = deque(trucks[1:])

    while trucks:
        cur_truck = trucks[0]

        if sum(bridge) + cur_truck <= weight:
            bridge.popleft()
            bridge.append(cur_truck)
            trucks.popleft()
            time += 1
        else:
            while True:
                if bridge[0] != 0:
                    bridge.popleft()
                    bridge.append(0)
                    time += 1
                    break
                bridge.popleft()
                bridge.append(0)
                time += 1
            if sum(bridge) + cur_truck <= weight:
                bridge[-1] = cur_truck
                trucks.popleft()
                if len(trucks) == 0:
                    break

    return time + bridge_length


if __name__ == "__main__":
    solution(3, 10, [4, 5, 6, 7])
    tmp = [4, 4, 5, 6, 7]
    tmp.remove(4)
    print(tmp)
