#https://www.codingame.com/training/medium/number-of-letters-in-a-number---binary
#NUMBER OF LETTERS IN A NUMBER-BINARY
import sys
import math
s,n=[int(i) for i in input().split()]
for i in range(n):
    l=3*bin(s)[2:].count("1")+4*bin(s)[2:].count('0') #'one','zero'
    #check the repeat pattern in outputs
    if l==s: break
    s=l
print(s)
