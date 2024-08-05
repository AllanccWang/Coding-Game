#https://www.codingame.com/training/medium/roman-sorting
#ROMAN SORTING
ROMAN_NUMBERS={1000=>"M",900 =>"CM",
500=>"D",400=>"CD",100=>"C",
90=>"XC",50=>"L",40=>"XL",
10=>"X",9=>"IX",5=>"V",
4=>"IV",1=>"I"}

def roman(n)
    roman = ""
    ROMAN_NUMBERS.each do |value, letter|
        roman << letter*(n / value)
        n = n % value
    end
    return roman
end

a=[]
gets.to_i.times do
  x = gets.to_i
  a+=[[x,roman(x)]]
end
puts a.sort_by{_1[1]}.map{_1[0]}*" "
