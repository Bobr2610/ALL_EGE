# from itertools import product
#
#
# cnt = 0
# b = [''.join(i) for i in product('135', repeat=2)]
# a = '0123456'
# for x in product(a, repeat=6):
#     t = True
#     s = ''.join(x)
#     if s[0] != '0':
#         if s.count('3') == 1:
#             for i in b:
#                 if i in s:
#                     t = False
#                     break
#             if t:
#                 cnt += 1
# print(cnt)


# print(sum(map(int, set([0, 1, 1, 2]))))
# cnt = 0
# with open('9.csv') as file:
#     f = file.readlines()
#     for i in f:
#         s = list(map(int, i.split(';')))
#         t = []
#         for j in s:
#             t.append(s.count(j))
#         if t.count(1) == 4 and t.count(3) == 3:
#             r = sum(map(int, set(s)))
#             w = (sum(map(int, s)) - r) / 2
#             e = r - w
#             if e / 4 < w:
#                 cnt += 1
# print(cnt)


# print(1020 + 10, 2 ** 11)
# print(95 * 11 / 8)
# print(65536 * 131 / 1024 )

# def f(n):
#     n = '7' + '1' * n
#     while '1111' in n or '7777' in n:
#         if '1111' in n:
#             n = n.replace('1111', '77', 1)
#         else:
#             n = n.replace('7777', '1', 1)
#     return sum(map(int, n))
#
#
# m = -9999
# for i in range(3 + 1, 1000):
#     m = max(f(i), m)
# print(m)


# q = []
# a = ['FSWY', 'SWYF', 'WYFS', 'YFSW']
# a2 = ['SWY', 'WY', 'Y']
# a3 = ['FSW', 'FS', 'F']
# with open('24.txt') as file:
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
# print(max(q))


q = []
s = ''
a = ['FSWY', 'SWYF', 'WYFS', 'YFSW']
# a2 = ['SWY', 'WY', 'Y']
a3 = ['FSW', 'FS', 'F']
with open('24.txt') as file:
    f = file.readline()
    cnt = 0
i = 0
mx = -9999
while i < len(f):
    if f[i:i + 4] in a:
        s += f[i:i + 4]
        i += 4
    elif 'FSWY' in s:
        if f[i:i + 3] in a3:
            s += f[i:i + 3]
            i += 3
        elif f[i:i + 2] in a3:
            s += f[i:i + 2]
            i += 2
        elif f[i:i + 1] in a3:
            s += f[i:i + 1]
            i += 1
        elif f[i] in a3:
            s += f[i]
            i += 0
        mx = max(len(s), mx)
print(mx)
