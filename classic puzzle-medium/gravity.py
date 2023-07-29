#https://www.codingame.com/training/medium/gravity
#GRAVITY
w,h=[int(i) for i in input().split()]
cnt=[0]*w #count the number of tiles per column
for i in range(h):
    line=input()
    for j in range(len(line)):
        if line[j]=="#":
            cnt[j]+=1
# #'s numbers per column if it above H_i than adding "#"
#H_i : numbers at that hieght
for h_i in range(h,0,-1):
    print("".join(["#" if cnt[j]>=h_i else "." for j in range(w)]))
