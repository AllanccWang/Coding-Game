#https://www.codingame.com/training/medium/dwarfs-standing-on-the-shoulders-of-giants
#dwarfs-standing-on-the-shoulders-of-giants -> path finding with nodes
import sys
import math

def count(node,edges):
    if node not in edges:return 1
    cnt=1
    for v in edges[node]:
        c=count(v,edges)
        cnt=max(cnt,c)
    return cnt+1

root=set()
edges=dict()

n=int(input()) # the number of relationships of influence
for i in range(n):
    # x: a relationship of influence between two people (x influences y)
    x,y=[int(j) for j in input().split()]
    edges.setdefault(x,[]).append(y)
    root.add(x)

for k in edges:
    for v in edges[k]:
        if v in root: root.remove(v)


cnt=0
for v in root:
    c=count(v,edges)
    cnt=max(c,cnt)

print(cnt)
