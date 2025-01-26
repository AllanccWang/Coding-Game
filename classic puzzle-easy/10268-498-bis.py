#problem: https://cpe.cse.nsysu.edu.tw/cpe/file/attendance/problemPdf/10268.pdf
fin=open(r"Input.txt",'r')
lines=[]
for items in fin:
    lines+=[items.rstrip()]
fin.close()

fout=open(r"Output.txt",'w')

for i in range(0,len(lines),2):
    x=int(lines[i])
    poly=list(map(int,lines[i+1].split()))[::-1]
    for k in range(len(poly)): poly[k]*=k
    #exclude the last parameter due to derivation
    poly=poly[1:]
    
    ans=0
    u=1
    for v in poly:
        ans+=u*v
        u*=x
    print(ans,file=fout)
fout.close()
