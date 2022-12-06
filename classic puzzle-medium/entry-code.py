#https://www.codingame.com/training/medium/entry-code
#entry-code
from itertools import product
s=[]
arr=int(input())
r=int(input())

#create all the combinations
for item in product([str(x) for x in range(arr)],repeat=r): s.append(item)
a=[]
for x in s:
  a.append(''.join([str(c) for c in x]))
a.sort()

#iterate and find the solution
v=[a[0]]
def f():
  if len(v)==len(a):
    ans=v[0]
    for i in range(1,len(a)):
      ans+=v[i][r-1:]
    print(ans)
    exit()
  for x in a:
    if x[:r-1]==v[-1][-(r-1):] and x not in v:
      v.append(x)
      f()
      v.pop()
  return
print(f())
