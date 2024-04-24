# a = open('27-8a.txt').readlines()
# q = []
# for i in range(1, len(a)-5):
#     o = []
#     print(a[i])
#     for j in range(i + 5, len(a)):
#         o.append(int(a[j]))
#     print(o)
#     if len(o) > 0:
#         q.append(int(a[i]) ** 2 + min(o) ** 2)
# print(min(q))

# def f(s):
#     if s.count('1') == s.count('0'):
#         s = s + s[-1]
#     else:
#         if s.count('1') < s.count('0'):
#             s = s + '1'
#         else:
#             s = s + '0'
#     return s
#
#
# for n in range(80, 2, -1):
#     a = f(f(f(f'{n:b}')))
#     r = int(a, 2)
#     if r % 2 == 0 and r % 4 != 0:
#         print(n)
#         break

# 3
# ip_ad = '224.32.48.131'
# ip = '224.32.32.0'
# for i in range(9):
#     a = '1' * i + '0' * (8 - i)
#     f = int(a, 2)
#     if 48 & f == 32:
#         print(f)
#

# 4
# g_o = 55
#
#
# def f(x1, x2, c, pob):
#     if x1 + x2 >= g_o or c > max(pob):
#         return c in pob
#     moves = [f(x1 + 2, x2, c + 1, pob), f(x1 * 2, x2, c + 1, pob), f(x1, x2 + 2, c + 1, pob), f(x1, x2 * 2, c + 1, pob)]
#     if c % 2 == max(pob) % 2:
#         return all(moves)
#     else:
#         return any(moves)
#
#
# print('\n#19')
# for s in range(1, 46):
#     if not f(9, s, 0, [1]) and f(9, s, 0, [2]):
#         print(s)
#         break
#
# print('\n#20')
# for s in range(1, 46):
#     if not f(9, s, 0, [1]) and f(9, s, 0, [3]):
#         print(s)
#         break
#
#
# print('\n#21')
# for s in range(1, 46):
#     if f(9, s, 0, [2, 4]) and not f(9, s, 0, [2]):
#         print(s)

# 5
# def f(n, k):
#     if n > k or n == 22:
#         return 0
#     elif n == k:
#         return 1
#     return f(n + 1, k) + f(n * 2, k)
#
#
# print(f(2, 15) * f(15, 31))