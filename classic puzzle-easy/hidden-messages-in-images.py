#https://www.codingame.com/training/easy/hidden-messages-in-images
#hidden-messages-in-images
import sys
import math

w,h=[int(i) for i in input().split()]
s=[]
for i in range(h):
    for j in input().split():
        pixel = int(j)
        s.append(bin(pixel)[2:][-1])
byte=""
for bits in s:
    byte+=bits
    if len(byte)==8:
        print(chr(int(byte,2)),end='')
        byte=""
