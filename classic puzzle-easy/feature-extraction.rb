#https://www.codingame.com/training/easy/feature-extraction
#FEATURE EXTRACTION
#concept: Dot product
r,c=gets.split.map &:to_i
a,w=[],[]
r.times{a+=[gets.split.map(&:to_i)]}
m,n=gets.split.map &:to_i
m.times{w+=[gets.split.map(&:to_i)]}
(0..r-m).map{|i|
  x=[]
  (0..c-n).map{|j|
    s=0
    for k in (0...m)
      (0...n).each do |l|; s+=a[i+k][j+l]*w[k][l]; end
    end
    x+=[s]
  }
  puts x*" "
}
