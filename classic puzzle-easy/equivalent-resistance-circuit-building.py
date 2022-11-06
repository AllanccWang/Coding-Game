#https://www.codingame.com/training/easy/equivalent-resistance-circuit-building
#equivalent-resistance-circuit-building
import math

n = int(input())
dy={}
for i in range(n):
    inputs = input().split()
    name = inputs[0]
    r = int(inputs[1])
    dy[name]=r #define dictionary for representation

circuit = input().split()
stack=[] #deal the braketed subcircuit with stack
for c in circuit:
    s=[]
    series,para=0,0
    if c==")":
        for i in stack[::-1]:
            if i!="(": s.append(i);stack.pop()
            else: break
        stack.pop()
        for i in s:
            if i in dy: series+=dy[i]
            else: series+=i
        #print("Series",series) #check the series resistance per subcircuit
    elif c==']':
        para=0
        for i in stack[::-1]:
            if i!="[": s.append(i);stack.pop()
            else: break
        stack.pop()
        for i in s:
            if i in dy: para+=(1/dy[i])
            else: para+=(1/i)
        para=1/para
        #print("Para",para) #check parallel resistance per subcircuit
    else:
        stack.append(c)

    if series: stack.append(series)
    elif para: stack.append(para)

    #print(stack,stack[-1]) # check the status in stack

print(f"{stack[-1]:.1f}")
