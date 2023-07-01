#https://www.codingame.com/training/easy/offset-arrays
#OFFSET ARRAYS
#concepts: Parsing/Recursion
n=gets.to_i

m=[]
#format A[-1..1] = 1 2 3 into [["A"], [-1, 0, 1], [1, 2, 3]]
n.times do
  s1,s2=gets.chomp.split("=")
  a=s1.scan(/[A-Z]+/)
  b=s1.scan(/[+-]?\d+/).map(&:to_i)
  b=(b[0]..b[1]).to_a
  c=s2.scan(/[+-]?\d+/).map(&:to_i)
  m+=[[a,b,c]]
end
#m.map{print _1,"\n"}
s=gets.chomp
idx=s.scan(/[+-]?\d+/).map(&:to_i)[0]
sign=s.scan(/[A-Z]+/).reverse.each{|arr|
  x=m.select{_1[0][0]==arr}[0]
  post=x[1].index(idx)
  idx=x[2][post]
}
print idx
