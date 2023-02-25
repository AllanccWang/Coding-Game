#https://www.codingame.com/training/hard/magic-count-of-numbers
#MAGIC COUNT OF NUMBERS
import math
from itertools import combinations

inputs = input().split()
n=int(inputs[0])
k=int(inputs[1])
count=0
prime=[int(i) for i in input().split()]
for i,a in enumerate(prime):
    cnt=0
    #case: n=30,p={2,3,5}
    #[30/2]+[30/3]+[30/5]-[30/(2*3)]-[30/(3*5)]-[30/(2*5)]+[30/(2*3*5)]
    #index=1,3,5... adding to var count
    #index=2,4,6... subtract to var count
    for gcd in list(combinations(prime,i+1)):
        cnt+=n//math.prod(gcd)
    count+=(-1)**i*cnt
print(count)
