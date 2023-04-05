def solution(tickets):
    res = list()

    def dfs(tickets, route):
        if not tickets:
            r = route.copy()
            res.append(r)

        else:
            start = route[-1]
            for t in tickets:
                if t[0] == start:
                    idx = tickets.index(t)
                    tic = t
                    route.append(tic[1])
                    tickets.pop(idx)
                    dfs(tickets, route)
                    route.pop()
                    tickets.insert(idx, tic)

    for t in tickets:
        if t[0] == "ICN":
            tmp = tickets.copy()
            route = []
            route.append(t[0])
            route.append(t[1])
            tmp.remove(t)
            dfs(tmp, route)

    res.sort()
    return res[0]
