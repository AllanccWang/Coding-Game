#https://www.codingame.com/training/easy/detective-pikaptcha-ep1
#DETECTIVE PIKAPTCHA EP1
#concept: Maze
STDOUT.sync=1
w,h=gets.split.map(&:to_i)
g=[]
h.times{
    line=gets.chomp
    g+=[line.chars]
}
dir=[[-1,0],[0,-1],[1,0],[0,1]]
h.times{|r|
    m=[]
    for c in (0...w)
        if g[r][c]=="0"
            cnt=0
            for d in dir
                x=r+d[0];y=c+d[1]
                cnt+=1 if x>=0&&x<h&&y<w&&y>=0&&g[x][y]=="0"
            end
            m+=[cnt]
        else
            m+=["#"]
        end
    end
    puts m*""
}
