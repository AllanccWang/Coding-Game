#https://www.codingame.com/training/easy/are-the-clumps-normal
#concept: Number theory
import sys
import math

n = input()
prev_num_clumps = 0
for b in range(2, 10):
    num_clumps = 0
    prev_clump = -1
    for d in n:
        if int(d) % b != prev_clump:
            num_clumps += 1
            prev_clump = int(d) % b

    if num_clumps < prev_num_clumps:
        print(b)
        exit()
    prev_num_clumps = num_clumps

print('Normal')
