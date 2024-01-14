#https://www.codingame.com/training/medium/huffman-code
#concept: Greedy algorithms / Compression / Trees
import sys
import math
class Node():
    def __init__(self,freq):
        self.freq = freq
        self.child = []
def dfs(node, code):
    size=0
    for i in range(0,len(node.child)):
        size+=dfs(node.child[i],code+["1","0"][i%2==0])
    if len(node.child)==0:
        return len(code)*node.freq
    return size

n = int(input())
tree=[] #building the relation tree
for i in input().split():
    wi = int(i)
    tree.append(Node(wi))
if len(tree)==1:
    print(tree[0].freq)
else:
    while len(tree)!=1:
        tree=sorted(tree, key=lambda x:x.freq)
        node1=tree.pop(0)
        node2=tree.pop(0)
        node=Node(node1.freq+node2.freq)
        node.child+=[node1,node2]
        tree.append(node)
    print(dfs(tree[0],""))
