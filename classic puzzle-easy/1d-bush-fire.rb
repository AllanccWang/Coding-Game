#https://www.codingame.com/training/easy/1d-bush-fire
'''
For example, if a water drop is targeted at cell 4, by splash effect it will put out fire in cell 3, 4 and 5 at the same time.
 _ _ _ _ _ _ _ _
|_|_|f|f|f|_|_|_
 1 2 3 4 5 6 7
 '''
gets.to_i.times{
  cnt=0
  index=0
  (line=gets.chomp).chars.each{
    if line[index]=='f'
      #puts index
      cnt+=1
      index+=3
    else
      index+=1
    end
  }
  puts cnt
}
