#https://www.codingame.com/training/medium/folding-paper
#folding-paper
import sys
import math

order = input()
side = input()
folds = {'R':1,'L':1,'U':1,'D':1}
for fold in order:
    for key in folds:
        if key!=fold:
            if (fold=='R' and key=='L') or (fold=='L' and key=='R') or (fold=='U' and key=='D') or (fold=='D' and key=='U'):
                folds[key]+=folds[fold]
            else:
                folds[key]*=2
    folds[fold]=1
    
print(folds[side])
