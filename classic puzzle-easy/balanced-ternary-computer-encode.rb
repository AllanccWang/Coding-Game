#https://www.codingame.com/training/easy/balanced-ternary-computer-encode
#BALANCED TERNARY COMPUTER: ENCODE
n=gets.to_i
s=""
while n.abs>0
    rem = n % 3
    n = n / 3
    if rem == 2
        rem = -1
        n+=1
    end
    s= (rem == 0 ? '0' : (rem == 1) ? '1' : 'T')+s
end
puts s!=''? s:0
