#10908-Largest-Square
#https://cpe.cse.nsysu.edu.tw/cpe/file/attendance/problemPdf/10908.pdf
fin=open(r"C:\Users\All\Desktop\PythonLab\Input.txt",'r')
stenc=[]
for items in fin:
    stenc+=[items.rstrip()]
fin.close()

fout=open(r"C:\Users\All\Desktop\PythonLab\Output.txt",'w')
M,N,T="","",""

def check_length(grid,r,c,chr):
    d=[-1,1]
    flag=True
    ln=1
    ans=1
    while flag:
        xl,xr=int(r)+ln*d[0],int(r)+ln*d[1]
        yl,yr=int(c)+ln*d[0],int(c)+ln*d[1]
        if xl>=0 and yl>=0 and yr<int(N) and xr<int(M):
            for i in range(xl,xr+1):
                for j in range(yl,yr+1):
                    if grid[i][j]!=chr:
                        flag=False
                        break
                if not flag: break
        else:
            flag=False
        if flag: 
            ln+=1
            ans+=2
    return ans
    
for i in range(1,len(stenc)):
    try:
        M,N,T=stenc[i].split()
        if M.isdigit() and N.isdigit() and T.isdigit():
            grid=[]
            for j in range(int(M)): 
                grid+=[stenc[i+j+1]]
            t=0
            print(stenc[i],file=fout)
            while t<int(T):
                #center of square
                r,c=map(int,stenc[int(M)+t+i+1].split())
                print(check_length(grid,r,c,grid[r][c]),file=fout)
                t+=1
    except ValueError:
        pass

fout.close()
