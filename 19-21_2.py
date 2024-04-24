g_o = 53


def f(x1, c, pob):
    if x1 >= g_o or c > max(pob) and x1 <= 60:
        return c in pob
    if x1 * 2 > 60:
        moves = [f(x1 + 1, c + 1, pob), f(x1 + 2, c + 1, pob)]
    else:
        moves = [f(x1 + 1, c + 1, pob), f(x1 + 2, c + 1, pob), f(x1 * 2, c + 1, pob)]
    if c % 2 == max(pob) % 2:
        return all(moves)
    else:
        return any(moves)


print('\n#19')
for s in range(1, g_o + 1):
    if not f(s, 0, [1]) and f(s, 0, [2, 4]) and not f(s, 0, [2]):
        print(s)
        break

print('\n#20')
for s in range(1, g_o + 1):
    if f(s, 0, [2, 4, 6]) and not f(s, 0, [2, 4]):
        print(s)

print('\n#21')
for s in range(1, g_o + 1):
    if f(s, 0, [1, 3]) and not f(s, 0, [1]) and not f(s, 0, [2]):
        print(s)
        break