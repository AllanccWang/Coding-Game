#834-Continued-Fractions
#https://cpe.cse.nsysu.edu.tw/cpe/file/attendance/problemPdf/834.pdf

fin=open(r"Input.txt",'r')
lines=[]
for items in fin:
    lines+=[items.rstrip()]
fin.close()

fout=open(r"Output.txt",'w')

for items in lines:
    num,denum=map(int,items.split())
    b=[]#[b0; b1, . . . , bn]
    while 1:
        bi=num//denum
        b.append(str(bi))
        tmp=denum
        denum=num-bi*denum
        num=tmp
        if num%denum==0: 
            b.append(str(num//denum))
            break

    print(f"[{b[0]};{','.join(b[1:])}]",file=fout)
    
fout.close()
