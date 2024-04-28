# 2
# from itertools import product


# def f(x, y, z, w):
#     return int(((not x) and (z <= y) and (not w)) or ((z == w) and ((x or y) <= w))) == 1


# for x, y, z, w in product([0, 1], repeat=4):
#     if f(x, y, z, w):
#         print(y , w, x, z)

# 5
# def f(g, u):
#     s = ''
#     while g > 0:
#         s += str(g % u)
#         g //= u
#     return s[::-1]


# def g(n):
#     r = f(n,3)
#     if n % 7 == 0:    
#         r = r + r[-3::]
#     else:
#         r = r + f(n%7, 3)
#     r = int(r, 3)
#     return r

# for i in range(1, 10000):
#     e = g(i)
#     if e > 369:
#         print(e)
#         break

# 7
# print(470*1024*8/1600/900/0.45)
# print(2**5)

# 8
# from itertools import product


# a = 0
# for x in product(sorted('МИЗАНТРОП'), repeat=5):
#     a += 1
#     s = ''.join(x)
#     if a%2 == 0 and s[0] == 'Н' and s.count('Р') == 2:
#         q = a

# print(q)


# 9
# cnt = 0
# with open('/home/student/Рабочий стол/w/28/9_13865.csv') as file:
#     f = file.readlines()
#     for i in f:
#         s = i.split(';')
#         s[-1] = str(int(s[-1]))
#         m = int(max(s)) + int(min(s))
#         sm = sum(map(int, s)) - m
#         u1 = 0
#         for j in s: 
#             u1 += s.count(j)
#         if (u1 == 7) and ((sm * 3) >= (m*2)):
#             print(s)
#             cnt += 1
# print(cnt)

# 11
# print(10, 4999)
# print(2*5, 2**13)
# print((10 * 5 + 13)/ 8)
# print(1500/30-8)


# 12
# def f(n):
#     a = '5' + '2' * n
#     while '72' in a or '522' in a or '2222' in a:
#         if '72' in a:
#             a = a.replace('72', '2', 1)
#         if '522' in a:
#             a = a.replace('522', '27', 1)
#         if '2222' in a:
#             a = a.replace('2222', '5', 1)
#     return sum(map(int, a)) == 22


# for i in range(4, 10000):
#     if f(i):
#         print(i)
#         break



# 13 Неверно
# print(f'{192:08b}', f'{168:08b}', f'{32:08b}', f'{48:08b}')
# print(f'{255:08b}', f'{255:08b}', f'{255:08b}', f'{192:08b}')
# print(f'{192:08b}', f'{168:08b}', f'{32:08b}', '11')
# cnt = 0
# a = [int('11000000', 2), int('01000000', 2), int('10000000', 2)]
# print(48 & 192)
# for i in range(1, 255):
#     if (i & 192) == 0:
#         if (f'{i:b}'.count('1') + 6) % 5 == 0:
#             cnt += 1
# print(cnt)
# 13
# from ipaddress import *

# net = ip_network('192.168.32.48/255.255.255.192', 0)
# cnt = 0

# for ip in net:
#     if bin(int(ip))[2:].count('1') % 5:cnt+=1
# print(cnt)

#  25

# from fnmatch import fnmatch

# d1 = 'ЧНЧЧНЧН77'
# w = '010010111'
# l = len(d1)
# for i in range(0, 10 ** 9, 7777):
#     s = str(i)
#     if s[-2::] == '77' and len(s) == l:
#         d = ''
#         for j in s:
#             d += str(int(j)%2)
#         if d == w:
#             print(i, int(i / 7777))

# 19 - 21
# g_o = 512


# def f(x1, c, pob):
#     if x1 >= g_o or c > max(pob):
#         return c in pob
#     moves = [f(x1 + 5, c + 1, pob), f(x1 + 4, c + 1, pob), f(x1 + 3, c + 1, pob), f(x1 + 2, c + 1, pob), f(x1 * 2, c + 1, pob)]
#     if c % 2 == max(pob) % 2:
#         return all(moves)
#     else:
#         return any(moves)


# print('\n#19')
# for s in range(1, 511 + 1):
#     if not f(s, 0, [1]) and f(s, 0, [2]):
#         print(s)
#         break

# print('\n#20')
# for s in range(1, 511 + 1):
#     if not f(s, 0, [1]) and f(s, 0, [3]):
#         print(s)


# print('\n#21')
# for s in range(1, 511 + 1):
#     if f(s, 0, [2, 4]) and not f(s, 0, [2]):
#         print(s)
#         break

