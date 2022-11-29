#https://www.codingame.com/training/medium/sum-of-divisors
#sum-of-divisors
#ref:https://www.geeksforgeeks.org/sum-divisors-1-n/
import sys
import math

n = int(input())
s=0
for i in range(1,n+1):
    s+=(n//i)*i
print(s)
