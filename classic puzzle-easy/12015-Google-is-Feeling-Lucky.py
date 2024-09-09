#12015-Google-is-Feeling-Lucky
#problem from : https://cpe.cse.nsysu.edu.tw/cpe/file/attendance/problemPdf/12015.pdf
fin=open(r"Input.txt",'r')
stenc=[]
for items in fin:
    stenc+=[items.rstrip().split()]
fin.close()

fout=open(r"Output.txt",'w')
cnt=1
for i in range(1,len(stenc),10):
    arr=stenc[i:i+10]
    high=max(arr,key=lambda x:int(x[1]))
    ans=[]
    for c in arr:
        if int(c[1])==int(high[1]):
            ans+=[c[0]]
    print(f"Case #{cnt}:",file=fout)
    for anss in ans:
        print(anss,file=fout)
    cnt+=1
fout.close()
