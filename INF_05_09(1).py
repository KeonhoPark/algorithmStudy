word = dict()
first = list(input())
second = list(input())

for f in first:
    word[f] = word.get(f, 0) + 1

for s in second:
    word[s] = word.get(s, 0) - 1

for key, val in word.items():
    if val != 0:
        print("no")
        flag = 1
        break

else:
    print("yes")

