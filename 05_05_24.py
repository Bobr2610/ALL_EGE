# from itertools import product

# def f(x, y, z, w):
#     return int((not (x or y)) and (not w) or (not (z or w)) and y) == 1


# for x, y, z, w in product([0, 1], repeat=4):
#     if f(x, y, z, w):
#         print(w, y, z, x)

# def f(n):
#     r = f'{n:b}'
#     if n % 3 == 0:
#         r = r + r[-2:]
#     else:
#         w = f'{((n % 3) * 3):b}'
#         r = r + w
#     return int(r, 2)


# a = []
# for n in range(10000):
#     r0 = f(n)
#     if r0 >= 195:
#         a.append(r0)
# print(min(a))

# print(920 * 1024 * 8 / 1280 / 960 / 0.85)
# print(2 ** 7)

# from itertools import product

# cnt = 0
# a = '0123456'
# for x in product(a, repeat=7):
#     s = ''.join(x)
#     d = 0
#     for i in s:
#         d += int(i)%2
#     if d == (7 - 2) and s[0] != '0':
#         cnt += 1
# print(cnt)

# cnt = 0
# with open('/home/student/Рабочий стол/w/05_05_2024/2_9.csv') as file:
#     f = file.readlines()
#     for i in f:
#         s = i.split(';')
#         s = [int(i1) for i1 in s]
#         t1 = (len(set(s)) == 6)
#         o = sum(map(int, s)) - sum(map(int, set(s)))
#         if t1:
#             s.remove(o)
#             s.remove(o)
#             s1 = sorted(s)
#             t2 = (s1[0] * s1[1] * s1[2]) > ((o)**2)
#             if t2:
#                 print(s1, o)
#                 cnt += 1
# print(cnt)

# print(2 ** 12, 4080+10)
# print(12 * 79/8)
# print(119 * 65536 / 1024)

# def f(a):
#     while '11' in a or '444' in a or '8888' in a:
#         if '11' in a:
#             a = a.replace('11', '4', 1)
#         if '444' in a:
#             a = a.replace('444', '88', 1)
#         if '8888' in a:
#             a = a.replace('8888', '1', 1)
#     return sum(map(int, a))


# m = -9999
# for i in range(4, 10000):
#     n = '8' + (i * '4')
#     m = max(f(n), m)
# print(m)

# from ipaddress import *

# net = ip_network('112.208.0.0/255.255.128.0', 0)
# cnt = 0

# for ip in net:
#     if bin(int(ip))[2:].count('1') % 11:cnt+=1
# print(cnt)

# def f(n, h):
#     s = 0
#     while n > 0:
#         if n % h > 9:
#             s += 1
#         n //= h
#     return s

# a = 4 * 3125 ** 2019 + 3 * 625 ** 2020 - 2 * 125 ** 2021 - 4 * 5 ** 2023 - 2024
# print(f(a, 25))

# def f(a):
#     for x in range(500):
#         d = int((not (x%a==0)) <= ((x%28==0)<=(not (x%49==0)))) == 1
#         if not d:
#             return False
#     return True


# for A in range(1, 10000):
#     if f(A):
#         print(A)

# def f(n):
#     if n <= 3:
#         return 2025
#     return 3 * (n - 1) * f(n - 2)

# print(f(2027)/f(2023))
# print(3 * (2024-1) * 3 * (2022-1))
# print(f(2027-4)/f(2023))

# a = []
# with open('/home/student/Рабочий стол/w/05_05_2024/2_17.txt') as file:
#     f = file.readlines()
#     f = [str(int(i)) for i in f]
#     m = -99999
#     for j in f:
#         if j[-2::] == 21:
#             m = max(int(j), m)
#     m = m**2
#     for i in range(len(f)-1):
#         t1 = (int(f[i][-2::] == '21' and len(f[i]) == 5) + int(f[i+1][-2::]) == '21' and len(f[i]) == 5) == 1
#         if (int(f[i]) ** 2 + int(f[i+1]) ** 2) > m:
#             a.append(int(f[i]) + int(f[i+1]))
# print(len(a), max(a))

g_o = 435

def f(x1, c, pob):
    if x1 >= g_o or c > max(pob):
        return c in pob
    moves = [f(x1 + 5, c+1, pob), f(x1 * 3, c+1, pob)]
    if c % 2 == max(pob)%2:
        return all(moves)
    else:
        return any(moves)
    
print('\n#19')
for s in range(1, 434+1):
    if not f(s, 0, [1]) and f(s, 0, [2]):
        print(s)
        break
print('\n#20')
for s in range(1, 434+1):
    if not f(s, 0, [1]) and f(s, 0, [3]):
        print(s)
print('\n#21')
for s in range(1, 434+1):
    if f(s, 0, [2, 4]) and not f(s, 0, [2]):
        print(s)
        break