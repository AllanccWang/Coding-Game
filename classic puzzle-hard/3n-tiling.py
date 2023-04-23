#https://www.codingame.com/training/medium/3n-tiling
#3×N TILING
#https://cs.stackexchange.com/questions/123463/3xn-tiling-problem-with-blocks-of-size-3x1-or-2x2
t = int(input())
mod=10**9+7
#grid with k=2 height
f2=[0,0,1,1,1,1]
for i in range(6,10**6+2):
    a=f2[i-2]%mod
    b=f2[i-3]%mod
    f2+=[(a+b)%mod]
#grid with k=3 height
f3=[1,1,1,2,3,4,8,13,19]
for i in range(9,10**6+1):
    a=f3[i-1]
    a=(a+3*f3[i-3])%mod
    a=(a-2*f3[i-4])%mod
    a=(a-f3[i-6]+f3[i-7]+f3[i-9])%mod
    f3+=[a]
for i in range(t):
    k,n=[int(j) for j in input().split()]
    if k==1:
        print([0,1][n%3==0])
    elif k==2:
        print([f2[n],f2[n+1]][n>=4])
    else:
        print(f3[n])
