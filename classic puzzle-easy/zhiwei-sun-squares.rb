#https://www.codingame.com/training/easy/zhiwei-sun-squares
#ZHIWEI SUN SQUARES
n=gets.to_i
l=(n**0.5).to_i+1
cnt=0
for b in (0...l)
    for c in (0...l)
        for d in (0...l)
            t=n-(b**2+c**2+d**2)
            if t<0
                break
            end
            a=t**0.5
            e=(b+3*c+5*d)**0.5
            cnt+=1 if e.floor==e && a.floor==a
        end
    end
end
puts cnt
