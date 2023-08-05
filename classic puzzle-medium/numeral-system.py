#https://www.codingame.com/training/medium/numeral-system
#NUMERAL SYSTEM
#concept: Parsing / Radix
import re
import math

eq=input()
s=re.findall(r'[0-9A-Z]+',eq)
r=1
for x in eq:
    t=-1
    if x.isalpha(): t=ord(x)-65+10
    elif x.isdigit(): t=int(x)
    r=max(r,t)
ans=36
for radix in range(36,r,-1):
    a=[int(x,radix) for x in s]
    if sum(a[0:2])==a[2]:
        ans=min(radix,ans)
print(ans)
