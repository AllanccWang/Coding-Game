#https://www.codingame.com/training/easy/moves-in-maze
#MOVES IN MAZE
#concept: Flood fill, BFS, Maze
fill=("0".."9").to_a+("A".."Z").to_a
w,h=gets.split(" ").map &:to_i
map=[]
x0,y0=0,0
h.times{
  map+=[gets.chomp]
  if map[-1].include?"S"
    x0=map.size-1
    y0=map[-1].index("S")
  end
}
stk=[[x0,y0,0]]
map[x0][y0]=fill[0]
dir=[[1,0],[-1,0],[0,-1],[0,1]]
while !stk.empty?
    pos=stk[-1]
    stk.pop
    for i in dir
        x=pos[0]+i[0]
        y=pos[1]+i[1]
        idx=pos[2]
        x=0 if x==h
        x=h-1 if x==-1
        y=0 if y==w
        y=w-1 if y==-1
        if map[x][y]=="."
            map[x][y]=fill[idx+1]
            stk.push([x,y,idx+1])
        end
    end
    stk=stk.sort_by{-_1[2]}
end
map.each{puts _1}
