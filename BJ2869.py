import math

a, b, v = map(int, input().split())

count = math.ceil((v-b)/(a-b))

print(count)