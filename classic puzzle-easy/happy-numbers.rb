#https://www.codingame.com/training/easy/happy-numbers
#HAPPY NUMBERS
gets.to_i.times do
  x=gets.chomp.to_i
  t=[x]
  while true
    x=x.digits.map{_1**2}.sum
    t.include?(x) ? break : t<<x
  end
  puts t[-1]==1 ? "#{t[0]} :)" : "#{t[0]} :("
end
