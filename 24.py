# a = []
# with open('24_1.txt') as file:
#     f = file.readline().strip()
#     e = ['FE', 'EF']
#     t = False
#     cnt = 0
#     for i in range(len(f) - 1):
#         if (f[i] + f[i+1]) in e:
#             cnt += 1
#             t = True
#         elif t:
#             a.append(cnt + 1)
#             t = False
#             cnt = 0
# print(max(a))

# from itertools import product
#
#
# sp = [''.join(i) for i in product('NOP', repeat=2)]
# a = []
# with open('24_2.txt') as file:
#     f = file.readline().strip()
#     t = False
#     cnt = 0
#     for i in range(len(f) - 1):
#         if (f[i] + f[i+1]) not in sp:
#             cnt += 1
#             t = True
#         elif t:
#             a.append(cnt + 1)
#             t = False
#             cnt = 0
# print(sp)
# print(max(a))


# sp = [str(i) for i in range(0, 10, 2)]
# a = []
with open('24_3.txt') as file:
    f = file.readline().strip()
#     t = False
#     cnt = ''
#     for i in range(len(f)):
#         if (f[i]) in sp:
#             cnt += f[i]
#             t = True
#             if i == len(f) - 1:
#                 a.append(int(cnt))
#                 break
#         elif t:
#             a.append(int(cnt))
#             t = False
#             cnt = ''
# print(sp)
# print(max(a))

alf = '02468'
cnt = ''
a = []
for char in f:
    if char in alf:
        cnt += char
    else:
        if cnt and char.isalpha():
            a.append(int(cnt))
        cnt = ''
print(max(a))