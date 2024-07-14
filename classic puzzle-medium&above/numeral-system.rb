#https://www.codingame.com/training/medium/numeral-system
#NUMERAL SYSTEM
#concept: Parsing / Radix
ss=gets
s=ss.scan(/[0-9A-Z]+/)
r=2
ss.chars.map{
    t=_1=~/[A-Z]/?_1.ord-64:_1.to_i
    r=[t,r].max
}
radix=36
(36..2).step(-1).map{|k|
    a=s.map{_1.downcase.to_i(k)}
    if a[0]+a[1]==a[2]&&k>=r
        radix=[k,radix].min
    end
}
puts radix
