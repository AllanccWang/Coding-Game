#11518-Dominos-2
#https://cpe.cse.nsysu.edu.tw/cpe/file/attendance/problemPdf/11518.pdf

fin=open("Input.txt",'r')
lines=[]
for items in fin:
    lines+=[items.rstrip()]
fin.close()

from collections import defaultdict
fout=open("Output.txt",'w')
cases=int(lines[0])
idx=1
while cases:
    n,m,l=map(int,lines[idx].split())
    domino=[1 for i in range(n+1)]
    idx=idx+1 #three integers n, m, l
    links=defaultdict(list)
    for i in range(idx,idx+m):
        x,y=map(int,lines[i].split())
        links[x].append(y)
    idx+=m
    for i in range(idx,idx+l):
        touch=int(lines[i])
        domino[touch]=0
        queue=[touch]
        while queue:
            pre=queue[0]
            queue=queue[1:]
            for k in links[pre]:
                if domino[k]==1:
                    domino[k]=0
                    queue.append(k)
    print(domino.count(0),file=fout)
    idx+=l
    cases-=1
fout.close()
