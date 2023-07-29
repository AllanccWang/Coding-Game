#https://www.codingame.com/training/medium/gravity
#GRAVITY
w,h=gets.split.map &:to_i
cnt=[0]*w #count the number of tiles per column
h.times{
  s=gets.chomp
  (0...s.size).map{cnt[_1]+=1 if s[_1]=="#"}
}
# #'s numbers per column if it above H_i than adding "#"
#H_i : numbers at that hieght
(h...0).step(-1).map{|hieght|
    puts (0...w).map{|l|cnt[l]>=hieght ? "#":"."}*""
}
