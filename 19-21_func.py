g_o = 166


def f(x1, c, pob, func=all):
    if x1 >= g_o or c > max(pob):
        return c in pob
    moves = [f(x1 + 2, c + 1, pob, func=func), f(x1 + 10, c + 1, pob, func=func)]
    for i in range(2, 85):
        if x1 * i <= (80 + x1):
            moves.append(f(x1 * i, c + 1, pob, func=func))
        else:
            break
    if c % 2 == max(pob) % 2:
        return func(moves)
    else:
        return any(moves)


print('\n#19')
for s in range(1, 165 + 1):
    if f(s, 0, [3], any):
        print(s)
        break
print('\n#20')
for s in range(1, 165 + 1):
    if f(s, 0, [3]) and not f(s, 0, [1]):
        print(s)
print('\n#21')
for s in range(1, 165 + 1):
    if f(s, 0, [2, 4]) and not f(s, 0, [2]):
        print(s)
        break