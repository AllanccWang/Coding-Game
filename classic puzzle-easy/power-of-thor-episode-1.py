#https://www.codingame.com/ide/puzzle/power-of-thor-episode-1
import sys, math

lightX, lightY, initialTX, initialTY = [int(i) for i in input().split()]
thorX=initialTX
thorY=initialTY
# game loop
while 1:
    remainingTurns = int(input())
    directionX=""
    directionY=""
    if thorY>lightY:
        directionY+="N"
        thorY-=1
    elif thorY<lightY:
        directionY+="S"
        thorY+=1
    if thorX>lightX:
        directionX+="W"
        thorX+=1
    elif thorX<lightX:
        directionX+="E"
        thorX-=1
    
    print(directionY+directionX)
