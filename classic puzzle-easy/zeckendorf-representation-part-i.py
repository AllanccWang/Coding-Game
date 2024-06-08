#https://www.codingame.com/training/easy/zeckendorf-representation-part-i
#concept: Recursion / Greedy algorithms / Arithmetic / Mathematics / Numbers
import sys
import math

def fib(num):
    if num<=1: return num
    i,j,tmp=0,1,0
    while j<=num: tmp=i;i=j;j+=tmp
    return i

n=int(input())
storage=[]
while n>0:
    cur=fib(n)
    storage.append(str(cur))
    n-=cur
    
print("+".join(storage))
