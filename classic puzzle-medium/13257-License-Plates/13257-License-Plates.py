#13257-License-Plates
#PROB. description: https://cpe.cse.nsysu.edu.tw/cpe/file/attendance/problemPdf/13257.pdf

#this method pass the run time error

fin=open(r'Input.txt', 'r', encoding="utf-8")
lines=[]
for items in fin:
    lines.append(items.rstrip())
fin.close()

fout=open(r'Output.txt', 'w', encoding="utf-8")
        
for cases in range(1,len(lines)):
    s=lines[cases]
    
    if len(s)<3:
        print("0",file=fout)
    else:
        check=[[0 for i in range(26)] for j in range(26)]
        c=[0 for i in range(26)]
        re=[0 for i in range(100002)]
        a=[[] for i in range(26)]

        a[ord(s[0])-ord('A')].append(0)
        a[ord(s[1])-ord('A')].append(1)
        
        for i in range(2,len(s)):
            j=ord(s[i])-ord('A')
            a[j].append(i)
            c[j]+=1
            if c[j]==1:
                re[2]+=1
                
        for i in range(3,len(s)):
            j=ord(s[i-1])-ord('A')
            c[j]-=1
            if c[j]==0: re[i]=re[i-1]-1
            else: re[i]=re[i-1]
        
        seq=0
        #instead of going through string
        #only check the position of letter
        for i in range(26):
            for j in range(26):
                if i==j and len(a[i])>1:
                    seq+=re[a[j][1]+1]
                elif i!=j and len(a[i])!=0 and len(a[j])!=0 and a[j][len(a[j])-1]>a[i][0]:
                        k = 0
                        l = len(a[j])
                        while k!=l:
                            temp = k+(l-k)//2
                            if a[j][temp]>a[i][0]:
                                l = temp
                            else:
                                k = temp+1
                        seq+=re[a[j][k]+1]
        print(seq,file=fout)
                
fout.close()
