#https://www.codingame.com/training/easy/max-area
#MAX AREA
import math
from operator import itemgetter
n=int(input())
a=[int(i) for i in input().split()]
area=0
for i in range(max(a),min(a),-1):
    b=[x for x in range(n) if a[x]>=i]
    #print(b)
    area=max(area,(max(b)-min(b))*i)
print(area)
