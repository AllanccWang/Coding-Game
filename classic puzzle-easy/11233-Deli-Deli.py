#11233-Deli-Deli
#https://cpe.cse.nsysu.edu.tw/cpe/file/attendance/problemPdf/11233.pdf

fin=open(r"Input.txt",'r')
lines=[]
for items in fin:
    lines+=[items.rstrip()]
fin.close()

fout=open(r"Output.txt",'w')

L,N=map(int,lines[0].split())
irregular=[]
for i in range(1,1+L):
    irregular.append(lines[i].split())
    
#test cases
for i in range(1+L,1+L+N):
    flag=False
    ans=""
    for items in irregular:
        if lines[i] in items:
            ans=items[1]
            flag=True
    if not flag:
        if lines[i][-2] not in ["a","e","i","o","u"] and lines[i][-1]=="y":
            ans=lines[i][:-1]+"ies"
        elif lines[i][-1] in ['o','s','x'] or lines[i][-2:] in ['ch','sh']:
            ans=lines[i]+"es"
        else:
            ans=lines[i]+"s"
    print(ans,file=fout)
fout.close()
