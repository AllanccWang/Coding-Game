#https://www.codingame.com/training/medium/ascii-art-glass-stacking
#ASCII ART : GLASS STACKING
#concept: Ascii Art
n=gets.to_i
l=0
#define number of layers
eq=lambda{|l|eval("(#{l})*(#{l+1})*0.5").to_i}
l+=1 while eq.call(l)<n
l-=1 if eq.call(l)>n
#layers
h=[" *** "," * * "," * * ","*****"]
(1..l).each{|layer|
    spaces=3*(l-layer)
    (0...4).each{|i|puts " "*spaces+[h[i]]*layer*" "+" "*spaces}
}
