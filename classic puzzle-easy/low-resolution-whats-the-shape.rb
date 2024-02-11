#https://www.codingame.com/training/easy/low-resolution-whats-the-shape
#concept: loop, geometry
w, h = gets.split.map { |x| x.to_i }
area=0.0
h.times{gets.chomp.chars.each{|c| area+=(c=='X')?1:0.5 if c!="."}}
area/=(w*h)
puts (area>0.8) ? "Rectangle" : (area>0.6)? "Ellipse": "Triangle"
