#https://www.codingame.com/training/easy/build-a-bookcase
#concept: Loops / Logic / Mathematics / Ascii Art
import sys
import math

h = int(input())-1
w = int(input())
nb = int(input())

#elements
roof="/"*(w//2)+["","^"][w%2]+"\\"*(w//2)
shell="|"+" "*(w-2)+"|"
floor="|"+"_"*(w-2)+"|"

def drawing(i,x,j,y):
    #l1: small level , n1: its numbers
    #l2: large level , n2: its numbers
    #print(i,x,j,y)
    l1,l2,n1,n2=0,0,0,0
    if j<i:
        l2,n2=i,x
        l1,n1=j,y
    else:
        l2,n2=j,y
        l1,n1=i,x

    print(roof)
    for t in range(n1):
        for tt in range(l1-1): print(shell)
        print(floor)

    for t in range(n2):
        for tt in range(l2-1): print(shell)
        print(floor)
    
#nb=x+y
#h=mx+ny, with m,n ~ l,l+1
l=h//nb
for i in range(l,l+2):
    for j in range(l,l+2):
        for x in range(1,nb+1):
            if h == i*(x)+j*(nb-x):
                drawing(i,x,j,nb-x)
                exit()
            elif i*(x)+j*(nb-x)>h:
                break
