#https://www.codingame.com/training/easy/messed-up-mosaics
#MESSED UP MOSAICS
#concept: Pattern recognition / Loops / String manipulation
import math
# Pass all custom cases, but fail at validators
n=int(input())
pattern=input()
l=len(pattern)
'''
for i in range(n):
    row=input()
    flag=0
    match_case=[]
    for j in range(l):
        if row[0]==pattern[j]:
            r_index=0
            p_index=j
            while pattern[p_index%l]==row[r_index] and r_index!=len(row)-1:
                p_index+=1
                r_index+=1
            if r_index==len(row)-1:
                flag=1
            else:
                match_case+=[r_index]
    if flag==0:
        if match_case[0]==1 and l!=1:match_case[0]-=1
        print(f"({match_case[0]},{i})")
        exit()
'''
'''
in forum, for solving validator 6
construct the “expected line” from the pattern, by concat (nb+1) pattern so that the “expected line” is longer than the line
try to find the line in the expected line
if you find, the line is ok
if you don’t find, find the possibility with only one diff.
'''
for i in range(n):
    row=input()
    flag=0
    s=""
    for j in range(l):
        if row[0]==pattern[j]:
            s=""
            k=0
            while k<=len(row):
                s+=pattern[(k+j)%l]
                k+=1
            if row in s:
                flag=1
    if flag==0:
        for j in range(2):
            for k in range(0,len(row)):
                if s[j+k]!=row[k]:
                    if k==1:k-=1
                    print(f"({k},{i})")
                    exit()
