n, m = map(int, input().split())
p_s = [0] * n
p_t = [0] * n

for i in range(n):
    s, t = map(int, input().split())
    p_s[i] = s
    p_t[i] = t
max_score = -1


def dfs(f, time, score_sum):
    global max_score
    if time > m:
        return
    if f == n:
        if max_score < score_sum:
            max_score = score_sum
        return
    else:
        dfs(f+1, time + p_t[f], score_sum + p_s[f])
        dfs(f+1, time, score_sum)


if __name__ == "__main__":
    dfs(0, 0, 0)
    print(max_score)
