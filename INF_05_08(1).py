n = int(input())
poem = dict()

for i in range(n):
    word = input()
    poem[word] = 0

for i in range(n-1):
    word = input()
    poem[word] = 1

for key, val in poem.items():
    if val == 0:
        print(key)

