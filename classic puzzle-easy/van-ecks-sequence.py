#https://www.codingame.com/training/easy/van-ecks-sequence
#VAN ECK'S SEQUENCE
import sys
import math

a1=int(input())
n=int(input())
d={}
next_num=a1
a=[]

for i in range(n):
    if next_num in d:x=i-d[next_num]
    else:x=0
    d[next_num]=i
    a+=[next_num]
    next_num=x
print(a[n-1])
