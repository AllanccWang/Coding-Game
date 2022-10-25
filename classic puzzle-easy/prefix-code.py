#https://www.codingame.com/ide/puzzle/prefix-code
import sys
import math

n = int(input())
dy={}
for i in range(n):
    inputs = input().split()
    b = inputs[0]
    c = int(inputs[1])
    dy[b]=chr(c)
s = input()
l,r=0,0
ans=""
while r<len(s):
    a=s[l:r+1]
    if a in dy:
        ans+=dy[a]
        l=r+1
    r+=1
if l!=len(s):
    print(f'DECODE FAIL AT INDEX {l}')
else: print(ans)
