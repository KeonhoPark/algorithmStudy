

def dy(n, l):
    if l[n-1] != 0:
        return l[n]
    else:
        l[0] = 1
        for i in range(1, len(data)):
            m = 0
            for j in range(i):
                if data[i] > data[j] and l[j] > m:
                    m = l[j]
            l[i] = m + 1
        return l[i]


if __name__=="__main__":
    n = int(input())
    data = list(map(int, input().split()))
    if n == 1:
        print(1)

    else:
        dp_inc = [0] * n
        dp_dec = [0] * n
        dy(n, dp_inc)
        ln = len(data)
        for i in range(ln // 2):
            data[i], data[ln - i - 1] = data[ln - i - 1], data[i]
        dy(n, dp_dec)

        m = 0
        for i in range(ln):
            if dp_inc[i] + dp_dec[ln-i-1] > m:
                m = dp_inc[i] + dp_dec[ln-i-1]

        print(m-1)
