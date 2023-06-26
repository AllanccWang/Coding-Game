#https://www.codingame.com/codegolf/easy/ascii-art-codesize
#ASCII ART - CODE GOLF
l=gets.to_i
h=gets.to_i
t=gets.upcase.scan(/[^\n]/).map{_1=~/[A-Z]/?_1.ord-65:26}
h.times{r=gets.scan(/.{#{l}}/);puts t.map{r[_1]}*""}
