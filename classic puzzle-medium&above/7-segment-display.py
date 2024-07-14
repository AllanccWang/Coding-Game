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

n=input()
c=input()
s=int(input())
for i in range(10):
    for k in range(5):
        digits[i][k]=digits[i][k].replace("#",c)

for i in range(5):
 t=''
 for x in n:
  t+=digits[int(x)][i][0]+digits[int(x)][i][1]*s+digits[int(x)][i][2]+" "
 if i%2==1:
    for j in range(s-1):
        print(t.rstrip())
 print(t.rstrip())
