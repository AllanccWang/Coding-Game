#160-Factors-and-Factorials
#https://cpe.cse.nsysu.edu.tw/cpe/file/attendance/problemPdf/160.pdf

fin=open(r"Input.txt",'r')
lines=[]
for items in fin:
    lines+=[items.rstrip()]
fin.close()

fout=open(r"Output.txt",'w')

import math

primes=[]
for i in range(2,100):
    flag=1
    for j in range(2,int(math.sqrt(i))+1):
        if i%j==0:
            flag=0
            break
    if flag: primes+=[i]

index=0
while lines[index]!='0':
    num=int(lines[index])
    index+=1
    arr=[]
    for i in range(2,num+1):
        if i in primes:
            arr+=[[i,0]]
    
    for factor in range(2,num+1):
        for prime in arr:
            if factor>=prime[0]:
                while not factor%prime[0]:
                    factor=factor//prime[0]
                    prime[1]+=1
                    
    print(f"{str(num).rjust(3)}! =",end="",file=fout)
    
    for i in range(0,len(arr),15):
        ans=[" "*6,""][i==0]
        ans+="".join([str(c[1]).rjust(3) for c in arr[i:i+15]])
        print(ans,file=fout)
    
fout.close()
