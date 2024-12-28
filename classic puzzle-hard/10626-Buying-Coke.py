#problem from https://cpe.cse.nsysu.edu.tw/cpe/file/attendance/problemPdf/10626.pdf
#the test time is not so efficient

fin=open(r"Input.txt",'r')
lines=[]
for items in fin:
    lines+=[items.rstrip()]
fin.close()

fout=open(r"Output.txt",'w')

dp=[[[0 for i in range(110)] for j in range(151)] for k in range(710)]
remain=0

def coin_changes(a,b,c):
    if a+5*b+10*c==remain:
        return 0
    if dp[a][b][c]!=0:
        return dp[a][b][c]
    dp[a][b][c]=1e9
    if c>=1:
        dp[a][b][c]=min(dp[a][b][c],coin_changes(a+2,b,c-1)+1)
    if a>=3 and c>=1:
        dp[a][b][c]=min(dp[a][b][c],coin_changes(a-3,b+1,c-1)+4)
    if b>=2:
        dp[a][b][c]=min(dp[a][b][c],coin_changes(a+2,b-2,c)+2)
    if b>=1 and a>=3:
        dp[a][b][c]=min(dp[a][b][c],coin_changes(a-3,b-1,c)+4)
    if a>=8:
        dp[a][b][c]=min(dp[a][b][c],coin_changes(a-8,b,c)+8)
    return dp[a][b][c]
    
cases=int(lines[0])
for case in range(1,len(lines)):
    buy,c1,c5,c10=map(int,lines[case].split())
    remain=c1+5*c5+10*c10-8*buy
    dp=[[[0 for i in range(110)] for j in range(151)] for k in range(710)]
    print(coin_changes(c1,c5,c10))
    
fout.close()
