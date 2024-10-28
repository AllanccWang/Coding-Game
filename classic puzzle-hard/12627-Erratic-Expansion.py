#12627-Erratic-Expansion
#problem: https://cpe.cse.nsysu.edu.tw/cpe/file/attendance/problemPdf/12627.pdf

fin=open(r"Input.txt",'r')
lines=[]
for items in fin:
    lines+=[items.rstrip()]
fin.close()

fout=open(r"Output.txt",'w')

def numberOfRed(k,r):
    if r==0: return 0
    if k==0: return 1
    if r<=2**(k-1):
        return 2*numberOfRed(k-1,r)
    else:
        return 2*3**(k-1)+numberOfRed(k-1,r-2**(k-1))
        
cases=int(lines[0])+1

for i in range(1,cases):
    k,a,b=map(int,lines[i].split())
    nbofRed=numberOfRed(k,b)-numberOfRed(k,a-1)
    print(f"Case {i}: {nbofRed}",file=fout)
    
fout.close()
