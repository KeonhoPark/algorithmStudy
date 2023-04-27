def solution(m):
    def dp_init(m):
        dp = [0 for _ in range(len(m))]
        dp[0] = m[0]
        dp[1] = max(m[0], m[1])

        return dp

    if len(m) == 3:
        return max(m)

    else:
        m_first = m[:len(m) - 1:]
        m_last = m[1:len(m):]

        dp_first = dp_init(m_first)
        dp_last = dp_init(m_last)

        for i in range(2, len(m_first)):
            dp_first[i] = max(m_first[i] + dp_first[i - 2], dp_first[i - 1])
            dp_last[i] = max(m_last[i] + dp_last[i - 2], dp_last[i - 1])

        if dp_first[-1] >= dp_last[-1]:
            return dp_first[-1]
        else:
            return dp_last[-1]
