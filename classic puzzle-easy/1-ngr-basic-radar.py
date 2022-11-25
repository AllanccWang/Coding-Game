#https://www.codingame.com/training/easy/1--ngr---basic-radar
#1. NGR - BASIC RADAR
import sys
from collections import defaultdict

n = int(input())
d=defaultdict(list)
for i in range(n):
    inputs=input().split()
    plate=inputs[0]
    radar=inputs[1]
    times=int(inputs[2])
    if plate not in d:
        d[plate].append(radar)
        d[plate].append(times)
        d[plate].append(0)
    else:
        k1=int(d[plate][0].split("-")[1])
        k2=int(radar.split("-")[1])
        dt=(d[plate][1]-times)*2.777*(10**-7)
        if abs((k1-k2)//dt)>=130:
            d[plate][2]=int(abs((k1-k2)//dt))

for k in dict(sorted(d.items(),key=lambda x:(x[0],x[1]))):
    if d[k][2]>130:print(k,d[k][2])
