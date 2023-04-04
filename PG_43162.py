def dfs(start, visited, computers, network):
    visited.append(start)
    network.append(start)

    for i in range(len(computers[start])):
        if computers[start][i] == 1 and i not in visited:
            dfs(i, visited, computers, network)

    return network


def solution(n, computers):
    visited = list()
    network_list = list()

    for i in range(n):
        network = list()
        if i not in visited:
            network_list.append(dfs(i, visited, computers, network))

    return len(network_list)


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
