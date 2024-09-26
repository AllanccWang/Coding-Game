#437-The-Tower-of-Babylon
#https://cpe.cse.nsysu.edu.tw/cpe/file/attendance/problemPdf/437.pdf

fin=open(r"Input.txt",'r')
lines=[]
for items in fin:
    lines+=[items.rstrip()]
fin.close()

fout=open(r"Output.txt",'w')

from itertools import permutations
idx=0
cases=1
while lines[idx]!='0':
    rows=int(lines[idx])
    idx+=1
    stk=[]
    for i in range(idx,idx+rows):
        x,y,z=map(int,lines[i].split())
        for ele in set(permutations([x,y,z],3)):
            stk.append(ele)
    #sorted all combination regarding to x-value, block[0]
    stk=sorted(stk,key=lambda x:x[0])
    high=[0 for i in range(len(stk))]
    maxH=0
    for i in range(len(stk)):
        high[i]=stk[i][2]
        for j in range(0,i):
            if stk[i][0]>stk[j][0] and stk[i][1]>stk[j][1]:
                if high[i]<high[j]+stk[i][2]:
                    high[i]=high[j]+stk[i][2]
        maxH=max(high[i],maxH)
    print(f"Case {cases}: maximum height = {maxH}",file=fout)
    cases+=1
    idx+=rows
    
fout.close()
