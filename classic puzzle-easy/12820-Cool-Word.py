#12820-Cool-Word
#PROB. description: https://cpe.cse.nsysu.edu.tw/cpe/file/attendance/problemPdf/12820.pdf

fin=open(r'Input.txt', 'r', encoding="utf-8")
lines=[]
for items in fin:
    lines.append(items.rstrip())
fin.close()

fout=open(r'Output.txt', 'w', encoding="utf-8")
        
#main function
def check_coolWord(word):
    collect=set(list(word))
    nbs_ltt=[]
    flag=True
    for c in collect:
        if word.count(c) not in nbs_ltt:
            nbs_ltt.append(word.count(c))
        else:
            flag=False
            break
    return (flag and len(collect)>=2)
    
idx=0
cases=1
while idx<len(lines):
    rows=int(lines[idx])+1
    coolWord=0
    for i in range(idx+1,idx+rows):
        coolWord+=check_coolWord(lines[i])
    print(f"Case {cases}: {coolWord}",file=fout)
    cases+=1
    idx+=rows

fout.close()
