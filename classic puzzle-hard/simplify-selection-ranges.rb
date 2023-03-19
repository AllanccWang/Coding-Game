#https://www.codingame.com/training/hard/simplify-selection-ranges
#SIMPLIFY SELECTION RANGES
n=gets.chomp[1...-1].split(",").map(&:to_i).sort
a=[]
t=[n[0]]
for i in (1...n.size)
    if n[i]-t[-1]==1
        t+=[n[i]]
    else
        t.size>=3?a+=["#{t[0]}-#{t[-1]}"]:t.each{|x|a+=[x.to_s]}
        t=[n[i]]
    end
end
t.size>=3?a+=["#{t[0]}-#{t[-1]}"]:t.each{|x|a+=[x.to_s]}     
puts a.join(",")
