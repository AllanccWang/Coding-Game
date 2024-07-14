#https://www.codingame.com/training/medium/carmichael-numbers
#concept: Recursion / Arithmetic
import sys
import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def power(x,y,mod):
    if y==0: 
        return 1
    temp=power(x,y//2,mod)%mod
    temp=(temp*temp)%mod
    if y%2==1:
        temp=(temp*x)%mod
    return temp

def isCarmichaelNumber(n):
    b=2
    while b<n:
        if math.gcd(b,n)==1:
            if power(b,n-1,n)!=1:
                return 0
        b=b+1
    return 1
n = int(input())

if isCarmichaelNumber(n) and not is_prime(n):
    print("YES")
else:
    print("NO")
