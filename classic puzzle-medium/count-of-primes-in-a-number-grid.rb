#https://www.codingame.com/training/medium/count-of-primes-in-a-number-grid
#COUNT OF PRIMES IN A NUMBER GRID
require 'prime'
r,c=gets.split(" ").collect{|x| x.to_i}
*m=$<.map{_1.split.map &:to_i}
t=[]
def prime_in_grid(r,c,m,t)
  for i in (0...r)
    for j in (0...c)
      (j...c).to_a.each{|x| 
        t<<m[i][j..x].join.to_i if Prime.prime?(m[i][j..x].join.to_i)
      }
    end
  end
end
prime_in_grid(r,c,m,t)
m=m.transpose
prime_in_grid(c,r,m,t)
print t.uniq.size
