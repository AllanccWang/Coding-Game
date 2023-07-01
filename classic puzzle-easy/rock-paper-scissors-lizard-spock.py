#https://www.codingame.com/training/easy/rock-paper-scissors-lizard-spock
#ROCK PAPER SCISSORS LIZARD SPOCK
import math

n=int(input())
duel=[]
dic={"R":0,"S":1,"P":2,"L":3,"C":4}

for i in range(n):
    inputs=input().split()
    duel+=[[int(inputs[0]),dic[inputs[1]]]]

rounds=int(math.log2(n))
#difference of p1 and p2 modulo five
def DUEL(p1,p2):
    diff=(p1[1]-p2[1])%5
    if diff==0:
        if p1[0]<p2[0]: return True
        else: return False
    elif diff == 1 or diff == 2:
        return True
    else:
        return False
seq=[duel]
for i in range(rounds):
    tmp=[]
    for j in range(0,len(duel),2):
        p1=duel[j]
        p2=duel[j+1]
        if DUEL(p1,p2):tmp+=[p1]
        else:tmp+=[p2]
    duel=tmp
    seq+=[duel]
print(duel[0][0])

#find the winning sequence
t=[]
for x in seq[-2::-1]:
    for c in range(len(x)):
        if x[c][0]==duel[0][0]:
            c=[c-1,c+1][c%2==0]
            t+=[x[c][0]]
            break
print(*t[::-1])
