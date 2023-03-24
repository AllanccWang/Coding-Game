#https://www.codingame.com/training/easy/unit-fractions
#UNIT FRACTIONS
import sys
import math

n = int(input())
for x in range(n+1,2*n+1):
    l=math.lcm(n,x)
    delta=l//n-l//x
    y=l/delta
    if int(y)==y:
        s=f"1/{n} = 1/{int(y)} + 1/{x}"
        print(s)
