#https://www.codingame.com/training/medium/minimal-number-of-swaps
#MINIMAL NUMBER OF SWAPS
n=gets
m=gets.split.map(&:to_i)
s=0
a=m.sort.reverse.each_with_index{|x,i|
  if x!=m[i]
    s+=1
  end
}
puts s/2
