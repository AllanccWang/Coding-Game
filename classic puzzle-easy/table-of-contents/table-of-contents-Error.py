#https://www.codingame.com/training/easy/table-of-contents
import re

lf=int(input())
n=int(input())
arr=[]
msg={}
'''
Original plan is to use hash to store the title number {>s : number}
But it fails at
Error:
1 A.........................................1
    1 AA....................................5
        1 AAA...............................8
            1 AAAA..........................8
                1 AAAAA.....................9
        2 AAB..............................10 -> Correct
            2 AABA.........................12 -> 1 AABA.........................12
                2 AABAA....................12 -> 1 AABAA....................12
                3 AABAB....................13 -> 2 AABAB....................13
                    1 AABABA...............14
'''
for i in range(n):
    entry=input().split()
    s=re.findall(r"\w+",entry[0])[0] #title
    shf=entry[0].count(">") #number of >s
    '''
    idx=1
    if i!=0: 
        if arr[-1]>=shf:
            #print(s)
            for j in range(len(arr)-1,-1,-1):
                if shf>=arr[j]:
                    k=j
                    while arr[k]>=arr[j]:
                        if k==0:break
                        k-=1
                    idx+=arr[k:j+1].count(shf)
                    #print(k,j)
                    break         
    arr+=[shf]
    '''
    if shf not in msg:
        msg[shf]=1
    else:
        msg[shf]+=1

    #number of dots per line
    ln=lf-len(s)-len(entry[1])-len(str(msg[shf]))-4*shf-1
    print("    "*shf+str(msg[shf])+" "+s+"."*ln+entry[1])
