#10858-Unique-Factorization
#https://cpe.cse.nsysu.edu.tw/cpe/file/attendance/problemPdf/10858.pdf
import math
fin=open(r"Input.txt",'r')
stenc=[]
for items in fin:
    stenc+=[items.rstrip()]
fin.close()

fout=open(r"Output.txt",'w')
ans=[]
buf=[]

def dfs(num):
    if num==1 and len(buf)>1:
        ans.append(buf[:])
        return
    pre=buf[-1] if buf else 2
    for i in range(pre,num+1):
        if num%i==0:
            buf.append(i)
            dfs(num//i)
            buf.pop()
            
for i in range(0,len(stenc)):
    num=int(stenc[i])
    if num==0: break
    ans.clear()
    dfs(num)
    print(len(ans),file=fout)
    for chr in ans:
        print(" ".join(map(str,chr)),file=fout)
            
fout.close()
