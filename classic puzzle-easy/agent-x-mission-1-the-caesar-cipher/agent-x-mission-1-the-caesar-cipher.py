#https://www.codingame.com/training/easy/agent-x-mission-1-the-caesar-cipher
#concept: Cryptography / Cipher
import sys
import math

cipher=input()
word=input()
delimiters=[' ', ',', '.', '?', ';', ':', '!']

for key in range(0,97):
    strtmp=""
    awrstr="" #fixed : while if it's delimeter, than take it as SP
    for char in cipher:
        c=(ord(char)-key-32+95)%95+32
        if chr(c) in delimiters:
            awrstr+=' '
        else:
            awrstr+=chr(c)
        strtmp+=chr(c)
    #print decode msg
    tmp=awrstr.split()
    #print(tmp)
    for ltt in tmp:
        if word==ltt:
            print(key)
            print(strtmp)
            exit()
