#https://www.codingame.com/training/easy/wheres-wally
#concept : Regular expressions / String manipulation / Ascii Art
import sys
import math

wally_w, wally_h = [int(i) for i in input().split()]
img=[]
pic=[]
for i in range(wally_h):
    wally_row = input()
    img+=[wally_row]
pic_w, pic_h = [int(i) for i in input().split()]
for i in range(pic_h):
    pic_row = input()
    pic+=[pic_row]
match=False
for y in range(0,pic_h-wally_h+1):
    for x in range(0,pic_w-wally_w+1):
        if match==False:
            match=True
            for w_y in range(0,wally_h):
                for w_x in range(0,wally_w):
                    if match==True:
                        if img[w_y][w_x].isspace()==False and img[w_y][w_x] != pic[y+w_y][x+w_x]:
                            match=False
        if match:
            print(f"{x} {y}")
            exit()
