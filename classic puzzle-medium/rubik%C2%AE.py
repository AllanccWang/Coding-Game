#https://www.codingame.com/training/medium/rubik%C2%AE
#RUBIK®
import sys
import math

n = int(input())
ans=n*n*2+(n*2+2*(n-2))*(n-2)
if n==1: ans=1
print(ans)
