# n, k 입력받아서 공백 기준으로 나누고 각각 변수 N, k에 넣음
# n = 동전의 갯수, k = 만들어야 하는 값
n, k = map(int, input().split())

count = 0
coin = []

# N번동안 동전을 입력받아서 coin 리스트에 int형으로 삽입
for i in range(n):
    coin.append(int(input()))

# j = n에서 0까지 k // coin[j] 를 구해서 count에 더해줌
# 동전의 가치가 k 보다 크면 k // coin[j] == 0 이기 때문에 count에 영향을 주지 않음
# k = k % coin[j] 를 통해 K의 앞자리수를 잘라준다.
# 동전의 가치가 k 보다 크면 k % coin[j] == k 이기 때문에 k에 영향을 주지 않음
for j in reversed(range(n)):
    count += k // coin[j]
    k = k % coin[j]

# 최종 계산된 count 출력
print(count)