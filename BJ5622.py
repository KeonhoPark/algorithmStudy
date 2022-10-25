w = list(input())
t = 0

for i in range(len(w)):
    if ord('A') <= ord(w[i]) <= ord('C'):
        t += 3
    elif ord('D') <= ord(w[i]) <= ord('F'):
        t += 4
    elif ord('G') <= ord(w[i]) <= ord('I'):
        t += 5
    elif ord('J') <= ord(w[i]) <= ord('L'):
        t += 6
    elif ord('M') <= ord(w[i]) <= ord('O'):
        t += 7
    elif ord('P') <= ord(w[i]) <= ord('S'):
        t += 8
    elif ord('T') <= ord(w[i]) <= ord('V'):
        t += 9
    elif ord('W') <= ord(w[i]) <= ord('Z'):
        t += 10

print(t)


