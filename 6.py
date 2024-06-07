from ipaddress import *


cnt = 0
net = ip_network('192.168.32.48/255.255.255.192', 0)
for ip in net:
    # ip = 192.168.32.0 ....
    b = bin(int(ip))[2::].zfill(32)
    # b = 11000000101010000010000000000000 ....
    print(b)
    cnt +=1
print(cnt)


