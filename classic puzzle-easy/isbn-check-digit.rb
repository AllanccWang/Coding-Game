#https://www.codingame.com/training/easy/isbn-check-digit
#ISBN CHECK DIGIT
a=[]
gets.to_i.times do
  isbn=gets.chomp
  s=isbn[...-1].scan(/[0-9]/)
  n=0
  if s.size==9&&isbn[-1]=~/[0-9|X]/
    l=10
    s[..-1].each{|x|n=n+l*x.to_i;l-=1}
    n%=11
    n=n+(isbn[-1]=='X'?10:isbn[-1].to_i)
    a+=[isbn] if n%11!=0
  elsif s.size==12&&isbn[-1]=~/[0-9]/
    l=1
    s[..-1].each{|x|
      n+=(l==1?x.to_i: 3*x.to_i)
      l*=-1
    }
    n=n%10+isbn[-1].to_i
    a+=[isbn] if n%10!=0
  else
    a+=[isbn]
  end
end
puts "#{a.size} invalid:"
puts a
