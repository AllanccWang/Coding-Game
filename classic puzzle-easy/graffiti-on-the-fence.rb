#https://www.codingame.com/training/easy/graffiti-on-the-fence
#GRAFFITI ON THE FENCE
l=gets.to_i
n=gets.to_i
fence=[]
n.times{fence+=[gets.split.map(&:to_i)]}
#overlapping intervals
fence=fence.sort
stack=[fence[0]]
for i in fence[1..]
  if stack[-1][0]<=i[0]&&i[0]<=stack[-1][-1]
    stack[-1][-1]=[stack[-1][-1],i[-1]].max
  else
    stack+=[i]
  end
end
#un_paint segments
f=0
st=0
stack.each{|x|
if x[0]>st
    puts [st,x[0]]*" "
    f=1
end
st=x[1]
}
if st!=l
    puts [st,l]*" "
    f=1
end
if f==0
    puts "All painted"
end
