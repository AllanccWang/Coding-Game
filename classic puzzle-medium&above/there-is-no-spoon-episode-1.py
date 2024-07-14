#https://www.codingame.com/training/medium/there-is-no-spoon-episode-1
#THERE IS NO SPOON - EPISODE 1
#concept: Lists/Simulation https://www.codingame.com/share-replay/729436755
import sys
import math

# Don't let the machines win. You are humanity's last hope...
w=int(input())  # the number of cells on the X axis
h=int(input())  # the number of cells on the Y axis
a=[]
for i in range(h):
    a+=[[x for x in input()]]

# Three coordinates: a node, its right neighbor, its bottom neighbor
for i in range(0,h):
    for j in range(0,w):
        if a[i][j]=="0":
            out=[[j,i]]
            for width in range(1,w):
                x=j+width
                if x<w and a[i][x]=="0":
                    out+=[[x,i]]
                    break
            if len(out)!=2:
                out+=[[-1,-1]]
            for height in range(1,h):
                x=i+height
                if x<h and a[x][j]=="0":
                    out+=[[j,x]]
                    break
            if len(out)!=3:
                out+=[[-1,-1]]
            ans=[]
            for c in out:
                x=str(c[0])
                y=str(c[1])
                ans+=[x,y]
            print(*ans)
