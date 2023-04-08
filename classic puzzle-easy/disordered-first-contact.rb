#https://www.codingame.com/training/easy/disordered-first-contact
#DISORDERED FIRST CONTACT

n=gets.to_i
m=gets.chomp
if n<0
    n.abs.times do
        t=''
        l=0
        (1..m.size).each{
            _1%2==1?t=t+m[l...l+_1]:t=m[l...l+_1]+t
            if t.size>=m.size
                break
            end
            l=_1+l
        }
        m=t
    end
    puts m
else
    x=0
    rr=0
    (1..m.size).each{
        rr+=_1
        x=_1
        if rr+_1>=m.size
            break
        end
    }
    s=""
    f=0
    if x%2==0
        s=m[rr..]
        f=1
    else
        rr+=x
    end
    for j in (1..n)
        if f==0
            t=m[0...x]
            l=x
            r=rr
            for i in (x..1).step(-1)
                if i%2==0
                    t=m[l...l+i]+t
                    l+=i
                else
                    t=m[r-i...r]+t
                    r-=i
                end
            end
        else
            l=0
            r=rr
            t=''
            for i in (x..1).step(-1)
                if i%2==0
                    t=m[l...l+i]+t
                    l+=i
                else
                    t=m[r-i...r]+t
                    r-=i
                end
            end
        end
        m=t
    end
    puts f==1?m+s:m
end
