#https://www.codingame.com/training/easy/create-the-longest-sequence-of-1s
#create-the-longest-sequence-of-1s
import sys
import math

b = input()
a=[i for i in range(len(b)) if b[i]=='0']
max_length=0
for i in a:
    s="".join(['1' if j==i else b[j] for j in range(len(b))])
    k=s.split("0")
    max_length=max(max_length,len(max(k,key=lambda x:x.count('1'))))
print(max_length)
