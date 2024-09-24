#13055-Inception
#https://cpe.cse.nsysu.edu.tw/cpe/file/attendance/problemPdf/13055.pdf

fin=open(r"Input.txt",'r')
lines=[]
for items in fin:
    lines+=[items.rstrip()]
fin.close()

fout=open(r"Output.txt",'w')

Dom=[] #seqences in people's dream
for i in range(1,len(lines)):
    query=lines[i]
    if query=="Kick":
        Dom=Dom[:-1]
    elif query=="Test":
        if not Dom:
            print("Not in a dream",file=fout)
        else:
            print(Dom[-1],file=fout)
    else:
        name=query.split()[1]
        Dom.append(name)
    
fout.close()
