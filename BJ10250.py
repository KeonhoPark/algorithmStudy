t = int(input())
for i in range(t):
    h, w, n = map(int, input().split())
    ho = int((n / h))
    floor = int((n % h))
    if floor == 0:
        print(h*100 + ho)
    elif floor != 0:
        print(floor*100 + (ho+1))
