#https://www.codingame.com/training/medium/binary-sequence
gets.to_i.times{
  x=gets.chomp.to_i(2)
  if x==0
    puts "0"
  else
    x-=1
    l=1
    while x>=l*2**(l-1)
      x-=l*2**(l-1)
      l+=1
    end
    n,x=x.divmod(l)
    n+=2**(l-1)
    puts n.to_s(2)[x]
  end
}
