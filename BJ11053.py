#수열의 길이를 입력받는다.
n = int((input()))

#수열에 들어갈 숫자들을 입력받아 리스트에 넣는다.
data = list(map(int, input().split()))

#수열의 원소마다 증가하는 부분수열의 길이를 담을 수 있는 리스트를 생성한다.
ans = [1 for num in range(n)]


for i in range(1, n):
    for j in range(i):
        #현재 원소 이전의 원소들 중 크기가 작고 부분수열의 길이가 큰 원소에 해당하면 현재원소를 그 부분원소의 증가하는 수열에 포함한다.
        if data[i] > data[j] and ans[i] <= ans[j]:
            ans[i] = ans[j] + 1

#최종적으로 가장 크기가 큰 수열 길이를 출력한다.
print(max(ans))
