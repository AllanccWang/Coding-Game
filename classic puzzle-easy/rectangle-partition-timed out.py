#https://www.codingame.com/training/easy/rectangle-partition
#concept: Arrays / Loops
w,h,cnt_x,cnt_y=[int(i) for i in input().split()]
arrx=[int(i) for i in input().split()]+[w]
arry=[int(i) for i in input().split()]+[h]

for i in range(0,cnt_x):
    for j in range(i+1,cnt_x+1):
        arrx+=[arrx[j]-arrx[i]]
arrx.sort()

for i in range(0,cnt_y):
    for j in range(i+1,cnt_y+1):
        arry+=[arry[j]-arry[i]]
arry.sort()

cnt=0

for x in arrx:
    for y in arry:
        if x==y: cnt+=1
        elif x<y: break

print(cnt)
