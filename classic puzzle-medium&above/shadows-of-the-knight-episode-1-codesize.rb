#SHADOWS OF THE KNIGHT - EPISODE 1 - CODE GOLF
#https://www.codingame.com/codegolf/medium/shadows-of-the-knight-episode-1-codesize
STDOUT.sync=1
c,d=gets.split.map &:to_i
i=gets.to_i
x,y=gets.split.map &:to_i
a,b=0,0
loop do
    l=gets
    d=y if l=~/U/
    b=y if l=~/D/
    c=x if l=~/L/
    a=x if l=~/R/
    puts [x=(c+a)/2,y=(d+b)/2]*" "
end
