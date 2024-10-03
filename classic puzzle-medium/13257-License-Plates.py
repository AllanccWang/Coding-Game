#13257-License-Plates
#PROB. description: https://cpe.cse.nsysu.edu.tw/cpe/file/attendance/problemPdf/13257.pdf

fin=open(r'Input.txt', 'r', encoding="utf-8")
lines=[]
for items in fin:
    lines.append(items.rstrip())
fin.close()

fout=open(r'Output.txt', 'w', encoding="utf-8")

#below method gets correct answer, but it's run time error
from itertools import combinations
for cases in range(1,len(lines)):
    ans=set(combinations(lines[cases],3))
    print(len(ans))

fout.close()
