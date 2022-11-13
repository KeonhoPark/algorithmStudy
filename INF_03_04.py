n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

new_list = sorted(n_list + m_list)

for i in range(len(new_list)):
    print(new_list[i], end=" ")


out = list(map(int, input().split()))
if out == new_list:
    print("true")