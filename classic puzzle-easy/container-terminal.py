#https://www.codingame.com/training/easy/container-terminal
#concept: stack
import sys
import math

'''
mimic the vector[stack] data structure
stk=['']
print(stk)
stk[0]+='C'
stk[0]+='C'
print(stk)
stk.append('C')
print(stk)
'''

for i in range(int(input())):
    line=input()
    stk=[line[0]]
    for c in range(1,len(line)):
        idx=-1
        for j in range(0,len(stk)):
            if stk[j][-1]>=line[c]:
                idx=j
                break
        if idx!=-1:
            stk[idx]+=line[c]
        else:
            stk.append(line[c])
    print(len(stk))
