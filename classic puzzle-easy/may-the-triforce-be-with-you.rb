#https://www.codingame.com/training/easy/may-the-triforce-be-with-you
#MAY THE TRIFORCE BE WITH YOU!
n=gets.to_i
l=2*n-1
for i in (0...n)
    if i==0
        puts "."+" "*(l-i-1)+"*"*(2*i+1)
    else
        puts " "*(l-i)+"*"*(2*i+1)
    end
end
for i in (0...n)
    s=" "*(n-i-1)+"*"*(2*i+1)+" "*(l-2*i)+"*"*(2*i+1)
    puts s
end
