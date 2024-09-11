#1292-Strategic-game
#https://cpe.cse.nsysu.edu.tw/cpe/file/attendance/problemPdf/1292.pdf

fin=open(r"Input.txt",'r')
lines=[]
for items in fin:
    lines+=[items.rstrip()]
fin.close()

fout=open(r"Output.txt",'w')

import re
idx=0
grid=[[0 for i in range(1501)] for j in range(1501)] #grid
'''
dp table below
0: No guard on this node
1: Guard on this node
'''
dp=[[0 for i in range(1501)] for j in range(2)]
visit=[0 for i in range(1501)]

def dfs_checking(root,nodes):
    visit[root]=1
    dp[root][0]=0
    dp[root][1]=1
    for i in range(nodes):
        if grid[root][i] and not visit[i]:
            dfs_checking(i,nodes)
            #If no guard on node, children must have guards
            dp[root][0]+=dp[i][1]
            #Place guard on node or child, whichever is minimal
            if dp[i][0]<dp[i][1]:
                dp[root][1]+=dp[i][0]
            else:
                dp[root][1]+=dp[i][1]
                
while idx<len(lines):
    nodes=int(lines[idx])
    idx+=1
    grid=[[0 for i in range(nodes)] for j in range(nodes)] #grid
    dp=[[0 for i in range(2)] for j in range(nodes)]
    visit=[0 for i in range(nodes)]

    for i in range(idx,idx+nodes):
        root=int(re.findall(r"([0-9]+):\(",lines[i])[0])
        #number of roads
        roads=list(map(int,lines[i].split()[1:]))
        for j in roads:
            grid[root][j]=1
            grid[j][root]=1

    dfs_checking(0,nodes)
    results=0
    if dp[0][0]<dp[0][1]:
        results=dp[0][0]
    else: 
        results=dp[0][1]
    print(results,file=fout)
    idx+=nodes
    
fout.close()
