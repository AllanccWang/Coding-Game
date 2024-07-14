#https://www.codingame.com/training/hard/simplify-selection-ranges
#SIMPLIFY SELECTION RANGES
import sys
import math
n=sorted(list(map(int,input()[1:-1].split(","))))
a=[]
t=[n[0]]
for i in range(1,len(n)):
    if n[i]-t[-1]==1:
        t+=[n[i]]
    else:
        if len(t)>=3:
            a.append(f'{t[0]}-{t[-1]}')
        else:
            for x in t:a.append(str(x))
        t=[n[i]]
if len(t)>=3:
    a.append(f'{t[0]}-{t[-1]}')
else:
    for x in t:a.append(str(x))
print(','.join(a))
