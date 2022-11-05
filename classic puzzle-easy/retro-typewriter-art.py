#https://www.codingame.com/training/easy/retro-typewriter-art
#RETRO TYPEWRITER ART
import math

t=input().split()
dy={'sp':" ",'bS':"\\",'sQ':'\''}
s=""
for x in t:
    n=0
    ss=""
    for c in x:
        if c.isdigit():n=n*10+int(c)
        else: ss+=c
    if ss=="":
        ss=str(n)[-1]
        n=n//10
    if ss=='nl':
        print(s)
        s=""
    elif ss in dy:
        s+=dy[ss]*n
    else:
        s+=ss*n
if s!="": print(s)
