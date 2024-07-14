#https://www.codingame.com/training/medium/gravity-tumbler
#GRAVITY TUMBLER
w,h=gets.split.map(&:to_i)
count=gets.to_i
#initialize the matrix
m=$<.map{
  s=_1.scan(/#+/).join
  s=s+"."*(w-s.size)
  s.chars
}
#rotate the matrix
for i in (0...count)
  t=m.transpose.map{_1.join}
  i==0?m=t.reverse.map{_1.chars}:m=t.map{_1.chars}
end
m.each{puts _1.join}
