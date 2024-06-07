# from itertools import product
#
#
# def f(x1, y1, z1, w1):
#     return (z1 and (not w1)) or (z1 == x1) or y1
#
#
# for x, y, z, w in product([0, 1], repeat=4):
#     if not f(x, y, z, w):
#         print(w, z, y, x)

# def f(e, s):
#     w = ''
#     while e > 0:
#         w += str(e%s)
#         e //= s
#     return w[::-1]
#
#
# mn = 9999
# for n in range(10000):
#     r = f(n, 3)
#     q = sum(map(int, r))
#     if q%3 == 0:
#         r += '212'
#     else:
#         r += f(q * 2, 3)
#     r = int(r, 3)
#     if r > 490:
#         mn = min(mn, r)
#         print(mn)

# print(540 * 1024 * 8 / (0.65 * 1024 * 768))

# from itertools import product
#
#
# cnt = 0
# for x in product('012345678', repeat=7):
#     s = ''.join(x)
#     t = s.count('6')
#     s = s.replace('2', '0').replace('4', '0').replace('6', '0').replace('8', '0')
#     s = s.replace('3', '1').replace('5', '1').replace('7', '1')
#     if t == 1 and '11' not in s and '00' not in s:
#         cnt += 1
# print(cnt)

# from itertools import permutations
#
#
# with open('9_25053188.csv') as file:
#     f = file.readlines()
#
# cnt = 0
# r = 0
# for i in f:
#     r += 1
#     s = list(map(int, i.split(';')))
#     c = 0
#     for j in s:
#         c += int(j % 2 == 0) - int(j % 2 != 0)
#     if c == 0:
#         if sum(map(int, s)) % 3 == 0:
#             for p1, p2, p3, p4, p5, p6 in permutations(s):
#                 if p1 + p2 == p3 + p4 == p5 + p6:
#                     print(r)
#                     break

# print(6 * 50 / 8)
# print(38 * 35)

# def f(a):
#     while '54' in a or '4444' in a or '7744' in a:
#         if '54' in a:
#             a = a.replace('54', '77', 1)
#         if '4444' in a:
#             a = a.replace('4444', '5', 1)
#         if '7744' in a:
#             a = a.replace('7744', '45', 1)
#     return (sum(map(int, a)) ** (1 / 2)) % 1 == 0
#
#
# for n in range(4, 10000):
#     if f('5' + '4' * n):
#         print(n)
#         break

# for x in range(27):
#     s1 = int(f'42{x}731', 27)
#     s2 = int(f'5{x}98{x}3', 27)
#     s3 = int(f'94{x}726', 27)
#     s = s1 + s2 + s3
#     if s % 26 == 0:
#         print(s // 26)

# b = [i for i in range(120, 180+1)]
#
#
# def f(a):
#     global b
#     for x in range(180):
#         if not ((x % a == 0) or ((x in b) <= ((not(x % 16 == 0)) or (x + a <= 204)))):
#             return False
#     return True
#
#
# for A in range(1, 10000):
#     if f(A):
#         print(A)

# def f(n):
#     if n < 11:
#         return n
#     if n >= 11 and n % 2 == 0:
#         return 2 * n - 3 + f(n - 2)
#     if n >= 11 and n % 2 != 0:
#         return 3 * n - 4 + f(n - 3)
#
#
# print(f(5500) - f(5497))
# print((2 * 5500 - 3) + (2 * 5498 - 3) + (2 * 5496 - 3) - (3 * 5497 - 4))

# with open('17_25053188.txt') as file:
#     f = file.readlines()
# f = list(map(int, f))
# m = -99999
# for i in f:
#     r = str(abs(i))
#     if len(r) == 4 and r[-2::] == '22':
#         m = max(i, m)
# mx = -999999
# cnt = 0
# for i in range(len(f)-2):
#     i0 = f[i]
#     i1 = f[i+1]
#     i2 = f[i+2]
#     if len({len(str(abs(i0))), len(str(abs(i1))), len(str(abs(i2)))}) == 3:
#         s = i0 + i1 + i2
#         if s >= m:
#             mx = max(s, mx)
#             cnt += 1
# print(cnt, mx)

g_o = 112


# def f(x1, c, pob, func=all):
#     if x1 >= g_o or c > max(pob):
#         return c in pob
#     moves = [f(x1 * 2, c + 1, pob, func=func)]
#     if x1 % 2 == 0:
#         moves.append(f(x1 + 2, c + 1, pob, func=func))
#     else:
#         moves.append(f(x1 + 1, c + 1, pob, func=func))
#     if c % 2 == max(pob) % 2:
#         return func(moves)
#     else:
#         return any(moves)
#
#
# print('\n#19')
# for s in range(1, 111 + 1):
#     if f(s, 0, [2], any):
#         print(s)
#         break
# print('\n#20')
# for s in range(1, 111 + 1):
#     if f(s, 0, [3]) and not f(s, 0, [1]):
#         print(s)
# print('\n#21')
# for s in range(1, 111 + 1):
#     if f(s, 0, [2, 4]) and not f(s, 0, [2]):
#         print(s)
#         break

# def f(n, k):
#     if n > k:
#         return 0
#     if n == k:
#         return 1
#     if n == 7:
#         return f(n + 1, k) + f(n * 2, k)
#     return f(n + 1, k) + f(n + 5, k) + f(n * 2, k)
#
#
# print(f(7, 35))

# with open('24_25053188.txt') as file:
#     f = file.readline().rstrip()
# d = {b: 0 for b in set(f)}
# mn = 10**10
# l = 0
# for i in range(len(f)):
#     d[f[i]] += 1
#     while d[f[l]] > 1:
#         d[f[l]] -= 1
#         l += 1
#     if 0 not in d.values():
#         mn = min(mn, i - l + 1)
# print(mn)

from fnmatch import fnmatch


def divs(n):
    d = set()
    for div in range(2, int(n**0.5)+1):
        if n % div == 0:
            d.add(div)
            d.add(n//div)
    return sum(d)


for i in range(2068, 10**9, 2068):
    if fnmatch(str(i), '193*7?'):
        if i % 2068 == 0:
            dv = divs(i)
            if dv % 7 == 0:
                print(i, dv)

