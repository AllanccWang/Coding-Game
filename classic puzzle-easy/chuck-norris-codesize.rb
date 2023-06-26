#https://www.codingame.com/codegolf/easy/chuck-norris-codesize
#UNARY - CODE GOLF
puts gets.chomp.chars.map{"%07b"%_1.ord}.join.scan(/((.)\2*)/).map{k=_1[0];[k[0]=='1'?0:"00","0"*k.size]}*" "
