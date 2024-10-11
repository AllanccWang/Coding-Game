#10903-Rock-Paper-Scissors-Tournament
#https://cpe.cse.nsysu.edu.tw/cpe/file/attendance/problemPdf/10903.pdf
fin=open(r'Input.txt', 'r', encoding="utf-8")
lines=[]
for items in fin:
    lines.append(items.rstrip())
fin.close()

fout=open(r'Output.txt', 'w', encoding="utf-8")

idx=0
rps=["rock","paper","scissors"]
while lines[idx]!="0":
    n,k=map(int,lines[idx].split())
    idx+=1
    arr=[[0,0] for i in range(n+1)]
    rounds=k*n*(n-1)//2
    for i in range(idx,idx+rounds):
        p1,m1,p2,m2=lines[i].split()
        v1=rps.index(m1)
        v2=rps.index(m2)
        p1=int(p1)
        p2=int(p2)

        if v2-v1==1 or v1-v2==2:
            arr[p2][0]+=1
            arr[p1][1]+=1
        elif v1-v2==1 or v2-v1==2:
            arr[p1][0]+=1
            arr[p2][1]+=1

    for i in range(1,n+1):
        anstr="-"
        if sum(arr[i])!=0:
            anstr=f"{arr[i][0]/sum(arr[i]):.3f}"
        if i==n:
            print(f"{anstr}\n",file=fout)
        else:
            print(f"{anstr}",file=fout)
    idx+=rounds
    
fout.close()
