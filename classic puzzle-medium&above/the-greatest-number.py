#https://www.codingame.com/training/hard/the-greatest-number
#THE GREATEST NUMBER
import re
n=int(input())
a=input().split()
s=re.findall(r'[0-9]',''.join(a))
num=''
if '-' in a:
    num='-'+''.join(sorted(s,key=lambda x:x))
    if '.' in a:
        num=num[:2]+'.'+num[2:]
else:
    num=''.join(sorted(s,key=lambda x:-int(x)))
    if '.' in a:
        num=num[:-1]+'.'+num[-1:]
if float(num).is_integer():
    if '.' in num: print(int(num[:num.index('.')]))
    else: print(int(num))
else:
    print(float(num))
