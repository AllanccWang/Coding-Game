#https://www.codingame.com/training/medium/gravity-tumbler
#GRAVITY TUMBLER
import re
import numpy as np
w,h=map(int,input().split())
count=int(input())
m=[]
for i in range(h):
    r=''.join(re.findall(r"#+",input()))
    m+=[list(r+(w-len(r))*".")]
#Use numpy to rotate the 2D matrix
arr=np.array(m)
for i in range(count):
    arr=np.rot90(arr)
    if i!=0: arr=arr[::-1]
for j in range(len(arr)):print(''.join(arr[j]))
