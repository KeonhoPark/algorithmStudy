n = int(input())
weight = list(map(int, input().split()))
left = list()
right = list()
choo = [100, 50, 20, 10, 5, 2, 1]
# 1번 자갈을 왼쪽 2번 자갈을 오른쪽에 배치
left.append(weight[0])
right.append(weight[1])

for i in range(2, n):
    # 양팔저울이 평형을 이루는 경우 i번 자갈을 왼쪽에 올린다.
    if sum(left) == sum(right):
        left.append(weight[i])
    # 양팔저울이 평형을 이루지 않는 경우 i번 자갈을 가벼운 쪽에 올린다.
    else:
        if sum(left) > sum(right):
            right.append(weight[i])
        elif sum(left) < sum(right):
            left.append(weight[i])

#왼쪽과 오른쪽의 차이를 구함
weight_sub = abs(sum(left) - sum(right))
count = 0

#무게차이를 추 리스트의 무게로 하나씩 나눠본다.
for c in choo:
    #추의 무게가 1이면 남은 무게가 그대로 추의 갯수가 된다.
    if c == 1:
        count += weight_sub
        break
    #추가 무게차이보다 무거우면
    while (weight_sub // c) != 0:
        #무게차이를 추로 나눈 몫이 추의 갯수가 되고 무게차이를 갱신해준다.
        count += (weight_sub // c)
        weight_sub = weight_sub % c

print(count)



