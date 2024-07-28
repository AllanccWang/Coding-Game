#https://www.codingame.com/training/easy/agent-x-mission-1-the-caesar-cipher
#concept:Cryptography / Cipher
import sys
import math

#only pass at #1, 2, 4, 6
'''
word is matched to i as key number is 0
Standard Output Stream:
0
q(zmkmq~m("w}4(pi~m("w}(nw}vl(|pm(|zikm{(wn(iomv|(`6
'''

cipher=input()
word=input()
delimiters=[' ', ',', '.', '?', ';', ':', '!']

for key in range(0,97):
    strtmp=""
    for char in cipher:
        c=(ord(char)-key-32+95)%95+32
        strtmp+=chr(c)
    #print decode msg
    tmp=strtmp.lower().split()
    for ltt in tmp:
        if word in ltt:
            print(key)
            print(strtmp)
            exit()
