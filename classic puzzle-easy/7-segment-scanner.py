#https://www.codingame.com/training/easy/7-segment-scanner
#7-SEGMENT SCANNER
import sys
import math

d={"0":' _ | ||_|',"1":"     |  |",
"2":" _  _||_ ","3":" _  _| _|",
"4":"   |_|  |","5":" _ |_  _|",
"6":" _ |_ |_|","7":" _   |  |",
"8":" _ |_||_|","9":" _ |_| _|"}
l1 = input()
l2 = input()
l3 = input()
for x in range(0,len(l1),3):
    s=l1[x:x+3]+l2[x:x+3]+l3[x:x+3]
    for y in d:
        if d[y]==s: print(y,end='')
