# g_o = 135
#
#
# def f(x1, c, pob):
#     if x1 >= g_o or c > max(pob):
#         return c in pob
#     moves = [f(x1 + 5, c + 1, pob), f(x1 * 3, c + 1, pob)]
#     if c % 2 == max(pob) % 2:
#         return all(moves)
#     else:
#         return any(moves)
#
#
# print('\n#19')
# for s in range(3, 100):
#     if not f(s, 0, [1]) and f(s, 0, [2]):
#         print(s)
#         break
#
# print('\n#20')
# for s in range(3, 100):
#     if not f(s, 0, [1]) and f(s, 0, [3]):
#         print(s)
#
#
# print('\n#21')
# for s in range(3, 100):
#     if f(s, 0, [2, 4]) and not f(s, 0, [2]):
#         print(s)
#         break

# q = []
# a = ['FSWY', 'SWYF', 'WYFS', 'YFSW']
# a2 = ['SWY', 'WY', 'Y']
# a3 = ['FSW', 'FS', 'F']
# with open('24') as file:
#     f = file.readline()
#     cnt = 0
#     t = False
#     for i in range(3, len(f)):
#         if not t:
#             if (f[i-3] + f[i-2] + f[i-1] + f[i]) not in a:
#                 if (f[i-2] + f[i-1] + f[i]) not in a2:
#                     if (f[i - 1] + f[i]) not in a2:
#                         if (f[i]) in a2:
#                             cnt += 1
#                             t = True
#                     else:
#                         cnt += 1
#                         t = True
#                 else:
#                     cnt += 1
#                     t = True
#             else:
#                 cnt += 1
#                 t = True
#         else:
#             if (f[i-3] + f[i-2] + f[i-1] + f[i]) not in a:
#                 if (f[i-2] + f[i-1] + f[i]) not in a3:
#                     if (f[i - 1] + f[i]) not in a3:
#                         if (f[i]) not in a3:
#                             t = False
#                             q.append(cnt)
#                             cnt = 0
#                         else:
#                             cnt += 1
#                             t = True
#                     else:
#                         cnt += 1
#                         t = True
#                 else:
#                     cnt += 1
#                     t = True
#             else:
#                 cnt += 1
#                 t = True

# from fnmatch import fnmatch
#
#
# for n in range(0, 10 ** 11, 98591):
#     if fnmatch(str(n), '123*45??1?') and n % 98591 == 0:
#         print(n, n / 98591)

# yxzw
# 001
# 100
# 110


# def f(n, k):
#     if n == 21 or n > k:
#         return 0
#     if n == k:
#         return 1
#     return f(n + 1, k) + f(n * 2, k) + f(n * 3, k)
#
#
# print(f(2, 9) * f(9, 27))


# q = 0
#
#
# def f(n):
#     while '7777' in n or '1111' in n:
#         if '1111' in n:
#             n = n.replace('1111', '77', 1)
#         else:
#             n = n.replace('7777', '11', 1)
#     return sum(map(int, n))


