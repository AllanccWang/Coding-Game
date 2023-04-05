#https://www.codingame.com/training/hard/7-segment-display
#7-SEGMENT DISPLAY
'''
Print the number at big size using characters.
input:
14790
#
4
output:
              ####   ####   ####
     # #    #      # #    # #    #
     # #    #      # #    # #    #
     # #    #      # #    # #    #
     # #    #      # #    # #    #
        ####          ####
     #      #      #      # #    #
     #      #      #      # #    #
     #      #      #      # #    #
     #      #      #      # #    #
                      ####   ####
'''
digits=[
[' # ','# #','   ','# #',' # '],#0
['   ','  #','   ','  #','   '],#1
[' # ','  #',' # ','#  ',' # '],#2
[' # ','  #',' # ','  #',' # '],#3
['   ','# #',' # ','  #','   '],#4
[' # ','#  ',' # ','  #',' # '],#5
[' # ','#  ',' # ','# #',' # '],#6
[' # ','  #','   ','  #','   '],#7
[' # ','# #',' # ','# #',' # '],#8
[' # ','# #',' # ','  #',' # '],#9
]
n=gets.scan(/\d/)
c=gets.chomp
s=gets.to_i
for i in (0..9)
    for j in (0..4)
        digits[i][j]=digits[i][j].gsub('#',c)
    end
end
for i in (0..4)
    t=''
    n.each{
        a=_1.to_i
        t+=digits[a][i][0]+digits[a][i][1]*s+digits[a][i][2]+" "
    }
    if i%2==1
        for j in (0...s-1)
            puts t.rstrip
        end
    end
    puts t.rstrip
end
