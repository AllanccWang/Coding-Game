#https://www.codingame.com/training/hard/the-balanced-centrifuge-problem
#the-balanced-centrifuge-problem
import sys
import math
def isPrime(k):
    for i in range(2,int(k**0.5)+1):
        if k%i==0:
            return False
    return True
n=int(input())
a=[0]*(n+1)
s=[]
for i in range(2,n):
    if isPrime(i) and n%i==0:
        a[i]=1
        s.append(i)
#remove all number, which is a sum of prime divisors
#dynamic programming to store the numbers can be sum of factors
for num in range(2,n+1):
    if a[num]==0:
        for i in s:
            if a[num-i]==1:
                a[num]=1
#to balance k identical test tubes, 1 ≤ k ≤ n, in an n-hole centrifuge
#if both k and n-k can be expressed as a sum of prime divisors of n.
c=0
for num in range(2,n+1):
    if a[num]==1 and a[n-num]==1:
        c+=1
print(c+1)
