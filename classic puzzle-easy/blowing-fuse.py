#https://www.codingame.com/training/easy/blowing-fuse
#BLOWING FUSE
import sys
import math

n,m,c=[int(i) for i in input().split()]
status=[False]*n
cc=[int(i) for i in input().split()]
current=0
max_current=0
for i in input().split():
    mx=int(i)-1
    if not status[mx]:
        current+=cc[mx]
        if current>c:
            print("Fuse was blown.")
            exit()
        if current>max_current:
            max_current=current
        status[mx]=not status[mx]
    elif status[mx]:
        status[mx]=not status[mx]
        current-=cc[mx]
    
print("Fuse was not blown.")
print(f"Maximal consumed current was {max_current} A.")
