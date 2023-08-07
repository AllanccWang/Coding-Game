#https://www.codingame.com/training/medium/ascii-art-glass-stacking
#ASCII ART : GLASS STACKING
#concept: Ascii Art
import sys
import math

n=int(input())
eq=lambda a : int(eval(f"({a})*({a+1})*0.5"))
l=0
while eq(l)<n: l+=1
if eq(l)>n: l-=1
h=[" *** "," * * "," * * ","*****"]
for layer in range(1,l+1):
    spaces=3*(l-layer)*" "
    for i in range(0,4):
        s=" ".join([h[i]]*layer)
        print(spaces+s+spaces)
