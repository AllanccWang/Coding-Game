#GOAL Your goal is to find the longest recurring substring in the input (ignoring case) 
#and returning a lower-case version of that string. 
#A recurring substring may share some of its characters with other occurrences. Example: abbabba => abba
import sys
import math

a = input().lower()

ans=1
anw=''
for n in range(1,len(a)):
    ss=[a[i:i+n] for i in range(0,len(a))]
    for x in ss:
        c=0
        for k in range(0,len(a)):
            if x==a[k:k+n]:
                c+=1
        if c>1 and len(x)>ans:
            ans=len(x)
            anw=x
if len(anw)==0:
    print("None")
else:
    print(anw)
