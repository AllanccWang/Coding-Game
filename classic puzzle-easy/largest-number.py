#https://www.codingame.com/training/easy/largest-number
#largest-number
import sys
import math

n=input()
d=int(input())

if int(n)%d==0:print(n);exit()
else:
    s=[]
    for i in range(len(n)):
        a=n[:i]+n[i+1:]
        if len(str(int(a)))==len(a): s.append(int(a)) #exclude leading zero cases
    for x in sorted(s,reverse=True):
        if x%d==0:print(x);exit()

    s=[]
    for i in range(len(n)):
        for j in range(i+1,len(n)):
            a="".join([n[x] for x in range(len(n)) if x!=i and x!=j])
            if len(str(int(a)))==len(a): s.append(int(a)) #exclude leading zero cases
    
    for x in sorted(s,reverse=True):
        if x%d==0:print(x);exit()
    print("0")
