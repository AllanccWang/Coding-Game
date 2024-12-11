#problem: https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=1051
fin=open(r'Input.txt', 'r', encoding="utf-8")
lines=[]
for items in fin:
    lines.append(items.rstrip())
fin.close()

fout=open(r'Output.txt', 'w', encoding="utf-8")

for cases in range(len(lines)-1):
    n=int(lines[cases])
    m=n**(1/2)
    if m*m == n:
        print("yes")
    else:
        print("no")
    
fout.close()
