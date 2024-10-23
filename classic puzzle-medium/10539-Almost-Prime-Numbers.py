#10539-Almost-Prime-Numbers
#problem: https://cpe.cse.nsysu.edu.tw/cpe/file/attendance/problemPdf/10539.pdf

fin=open(r"Input.txt",'r')
lines=[]
for items in fin:
    lines+=[items.rstrip()]
fin.close()

fout=open(r"Output.txt",'w')

MAX=10**12
isPrime=[1 for i in range(1000000)]
almostPrime=[]

def allPrimes():
    isPrime[0]=0
    isPrime[1]=0
    for i in range(2,len(isPrime)):
        if i*i<len(isPrime) and isPrime[i]:
            for j in range(i*i,len(isPrime),i):
                isPrime[j]=0
               
def almostPrimes():
    allPrimes()
    for i in range(2,len(isPrime)):
        if isPrime[i]:
            pow=i*i
            while pow<=MAX:
                almostPrime.append(pow)
                if MAX/i<pow: break
                pow*=i
    almostPrime.sort()

almostPrimes()
def LowboundaryCheck(target):
    right=len(almostPrime)-1
    left=0
    pos=len(almostPrime)
    while left<right:
        mid=(left+right)//2
        if almostPrime[mid]<target:
            left=mid+1
            pos=left
        else:
            right=mid
    if almostPrime[left]>=target:
        pos=left
    return pos
        
def HighboundaryCheck(target):
    right=len(almostPrime)-1
    left=0
    pos=len(almostPrime)
    while left<right:
        mid=(left+right)//2
        if almostPrime[mid]<=target:
            left=mid+1
        else:
            right=mid
            pos=right
    if almostPrime[left]>target:
        pos=left
    return pos
    
for cases in range(1,int(lines[0])+1):
    Lo,Hi=map(int,lines[cases].split())
    cnt=HighboundaryCheck(Hi)-LowboundaryCheck(Lo)
    print(cnt,file=fout)
    
fout.close()
