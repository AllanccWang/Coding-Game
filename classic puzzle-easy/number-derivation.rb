#https://www.codingame.com/training/easy/number-derivation
#NUMBER DERIVATION
require 'prime'
n=gets.to_i
a=Prime.prime_division(n)
if a.size==1
    puts a[0][1]==1 ? 1 : a[0][1]*a[0][0]**(a[0][1]-1)
else
    ans=0
    for x in (0...a.size)
        s=[]
        for y in (0...a.size)
            if a[x]!=a[y]
                a[y][1]==1 ? s<<a[y][0] : s<<a[y][1]*a[y][0]**(a[y][1]-1)
            end
        end
        a[x][1]==1 ? ans+=s.reduce(&:*) : ans+=(a[x][1]*a[x][0]**(a[x][1]-1))*s.reduce(&:*)
    end
    print ans
end
