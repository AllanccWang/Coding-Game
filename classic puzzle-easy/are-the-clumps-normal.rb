#https://www.codingame.com/training/easy/are-the-clumps-normal
#concept: Number theory
n=gets.chomp
prev_num_clumps = 0
(2...10).each{|b|
    nb_clumps=0
    prev_val=-1
    n.chars.each{|d|
        if d.to_i%b!=prev_val
            nb_clumps+=1
            prev_val=d.to_i%b
        end
    }
    if nb_clumps<prev_num_clumps
        puts b
        exit
    end
    prev_num_clumps=nb_clumps
}
puts "Normal"
