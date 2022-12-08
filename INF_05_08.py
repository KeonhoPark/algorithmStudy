n = int(input())
note = list()
poem = list()

for i in range(n):
    note.append(input())

for i in range(n-1):
    poem.append(input())

for n in note:
    if not(n in poem):
        print(n)
        break

