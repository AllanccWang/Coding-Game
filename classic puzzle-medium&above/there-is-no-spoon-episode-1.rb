#https://www.codingame.com/training/medium/there-is-no-spoon-episode-1
#THERE IS NO SPOON - EPISODE 1
#concept: Lists/Simulation https://www.codingame.com/share-replay/729436755
STDOUT.sync = 1
# Don't let the machines win. You are humanity's last hope...

w=gets.to_i # the number of cells on the X axis
h=gets.to_i # the number of cells on the Y axis
a=[]
h.times{a+=[gets.chars]}
# Three coordinates: a node, its right neighbor, its bottom neighbor
(0...h).each{|i|
    for j in (0...w)
        if a[i][j]=="0"
            out=[[j,i]]
            (1...w).each{|times|
                x=j+times
                if x<w&&a[i][x]=="0"
                    out+=[[x,i]]
                    break
                end
            }
            (out.size...2).each{out+=[[-1,-1]]} if out.size!=2
            (1...h).each{|times|
                x=i+times
                if x<h&&a[x][j]=="0"
                    out+=[[j,x]]
                    break
                end
            }
            (out.size...3).each{out+=[[-1,-1]]} if out.size!=3
            puts out*" "
        end
    end
}
