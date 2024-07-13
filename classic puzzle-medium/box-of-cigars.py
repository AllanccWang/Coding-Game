#https://www.codingame.com/training/medium/box-of-cigars
#concept: Sequences / Mathematics

import sys
import math

cnt=0
ans=0
arr=[]
n=int(input())
for i in range(n):
    lnt=int(input())
    arr.append(lnt)

#checking the common diff
def checking_diff(j,d):
    global cnt
    for i in range(j+1,n):
        tmp=arr[i]-arr[j]
        if tmp==d:
            cnt+=1
            checking_diff(i,d)
        elif tmp>d:
            return
    return
#remove duplicates number
arr=list(set(arr))
n=len(arr)
for i in range(n-1):
    for j in range(i+1,n):
        cnt=2
        checking_diff(j,arr[j]-arr[i])
        ans=max(ans,cnt)
print(ans)
