#https://www.codingame.com/training/easy/tricky-number-verifier
#concept: Check-digit / String manipulation
import sys
import math
from datetime import datetime

def print_validity(str):
    if len(str)!=10 or str[0]=='0' or not str.isdigit():
        return print("INVALID SYNTAX")
    d,x,date=str[:3],str[3],str[4:]
    try:
        datetime.strptime(date,"%d%m%y")
    except ValueError:
        return print("INVALID DATE")
    tt=sum(int(i)*int(m) for i,m in zip(str, '3790584216')) % 11
    if tt==10:
        print_validity(f'{int(d) + 1}0{date}')
    elif int(x) != tt:
        print(f'{d}{tt}{date}')
    else:
        print('OK')

n=int(input())
for i in range(n):
    print_validity(input())
