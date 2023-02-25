#https://www.codingame.com/training/medium/the-fastest
#THE FASTEST
n=gets.to_i
m=1e7
winner=''
n.times do
  s=gets.chomp
  t=s.split(":").map(&:to_i)
  time=t[0]*60*60+t[1]*60+t[0]
  if time<=m
    m=time
    winner=s
  end
end

puts winner
