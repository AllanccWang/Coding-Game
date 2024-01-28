#https://www.codingame.com/training/medium/bust-speeding-vehicles
l = gets.to_i
n = gets.to_i
nb=0
record=[]
n.times{|i|
  r = gets.split
  plate=r[0]
  c=r[1].to_i
  t=r[2].to_i
  #puts record[-1]
  if i>0 && plate==record[-1][0] && (3600.0*(c-record[-1][1])/(t-record[-1][2]) > l)
    nb+=1
    puts "#{plate} #{c}"
  end
  record.push([plate,c,t])
}
puts "OK" if nb==0
