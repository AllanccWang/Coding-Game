#https://www.codingame.com/training/medium/sandpile-addition
#SANDPILE ADDITION
n=int(input())
m1=[[int(j) for j in input()] for i in range(n)]

for i in range(n):
    r = input()
    for j in range(len(r)):
        m1[i][j]+=int(r[j])

#check the grains per pile
def check_grains(m):
    for i in range(n):
        for j in m[i]:
            if j>=4:
                return False
    return True

while not check_grains(m1):
    for i in range(n):
        for j in range(len(m1)):
            if m1[i][j]>=4:
                g=m1[i][j]//4
                m1[i][j]%=4
                #adding grains to neighbors
                if i+1<n:m1[i+1][j]+=g
                if j+1<n:m1[i][j+1]+=g
                if i-1>=0:m1[i-1][j]+=g
                if j-1>=0:m1[i][j-1]+=g
for x in range(n):
    print(''.join([str(c) for c in m1[x]]))
