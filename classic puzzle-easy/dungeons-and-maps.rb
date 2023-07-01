#https://www.codingame.com/training/easy/dungeons-and-maps
#DUNGEONS AND MAPS
#concepts: Strings/Pathfinding/Loops/2D array
w,h=gets.split(" ").collect{|x|x.to_i}
x0,y0=gets.split(" ").collect{|x|x.to_i}

n=gets.to_i
dir=[[1,0],[-1,0],[0,-1],[0,1]]
sign="v^<>"

ans=[]
n.times{
  m=[]
  h.times{m+=[gets.chomp.chars]}
  stk=[[x0,y0,0]]

  while !stk.empty?
    pos=stk.pop
    x=pos[0]
    y=pos[1]
    if sign.include?(m[x][y])
      xp,yp=dir[sign.index(m[x][y])][0],dir[sign.index(m[x][y])][1]
    #if finding the Treasure!!!
    elsif m[x][y]=="T"
      ans+=[[_1,pos[2]]]
      break
    else
    #no Treasure and no sign for next step TT
      break
    end
    #Your next step
    stk+=[[x+xp,y+yp,pos[2]+1]] if x+xp>=0&&x+xp<h&&y+yp>=0&&y+yp<w
    #Going into a TRAP, a loop
    break if pos[2]>10**3
  end
}
puts ans.size!=0?ans.sort_by{_1[1]}[0][0]:"TRAP"
