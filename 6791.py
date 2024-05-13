with open('26-129.txt') as file:
    n = int(file.readline())
    f = file.readlines()
    a = []
    for i in range(1, n+1):
        x, y = map(int, f[i-1].split())
        a.append([x, i, True])
        a.append([y, i, False])
    a = sorted(a)
    b = [-1 for i in range(n)]
    c = []
    f = 0
    l = -1
    cnt = []
    for i in a:
        if i[1] not in c:
            if i[2]:
                b[f] = i
                cnt = [i, f]
                f += 1
            else:
                b[l] = i
                cnt = [i, l]
                l -= 1
            c.append(i[1])
print(cnt)
print(a)
print(b)
