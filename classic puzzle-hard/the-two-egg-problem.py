#https://www.codingame.com/training/hard/google-interview---the-two-egg-problem
import sys
import math

n=int(input())
x=1/2*(-1.0 + math.sqrt(1.0+8.0*n))
print(math.ceil(x))
