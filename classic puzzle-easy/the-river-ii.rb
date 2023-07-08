#https://www.codingame.com/training/easy/the-river-ii-
#THE RIVER II
#concept: Arithmetic
r1=gets.to_i
(r1-1..1).step(-1).map{|r2|
    l=r2+r2.digits.sum
    if l==r1
        puts "YES"
        exit
    end
}
puts "NO"
