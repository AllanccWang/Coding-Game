#https://www.codingame.com/training/medium/primitive-pythagorean-triples
#PRIMITIVE PYTHAGOREAN TRIPLES
import math
cnt=0
c=int(input())
#https://mathworld.wolfram.com/PythagoreanTriple.html
for n in range(1,math.ceil(c**0.5)):
    for m in range(n+1,math.ceil(c**0.5)):
        if math.gcd(m,n)==1 and (m+n)%2==1 and m*m+n*n<=c:
            cnt+=1
print(cnt)
