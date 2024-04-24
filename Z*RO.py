from fnmatch import fnmatch

c = 0
a = open('24-s1.txt').readlines()
for i in a:
    if fnmatch(i, '*Z?RO*'):
        c += 1
print(c)