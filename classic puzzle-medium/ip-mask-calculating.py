#https://www.codingame.com/training/medium/ip-mask-calculating
#IP MASK CALCULATING
ip=input().split("/")
s=int(ip[1])*'1'+(32-int(ip[1]))*'0'
mask=[int(s[x:x+8],2) for x in range(0,len(s),8)]
net=[int(x) for x in ip[0].split('.')]
subnet=[str(int(bin(ioctet & moctet), 2)) for ioctet, moctet in zip(net, mask)]
broadcast=[str((ioctet | ~moctet) & 0xff) for ioctet, moctet in zip(net, mask)]
print('.'.join(subnet))
print('.'.join(broadcast))
