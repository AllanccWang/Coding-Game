#https://www.codingame.com/training/easy/rectangle-partition
#refer: https://github.com/Aikeko/Codingame-Practice/blob/master/Rectangle%20Partition
#concept: Arrays / Loops
import sys
import math

w, h, count_x, count_y = [int(i) for i in input().split()]
measureX = [int(i) for i in input().split()]
measureY = [int(i) for i in input().split()]


def mergeDict(dict1, dict2):
    dict3 = {**dict1, **dict2}
    for key, value in dict3.items():
        if key in dict1 and key in dict2:
            dict3[key] = value + dict1[key]
    
    return dict3
    
def countUnique(cutsList):
    #print("countUnique start with list ", list)
    unique = set(cutsList)
    result = {}
    for i in unique:
        result[i] = cutsList.count(i)
    
    return result
    
def getCuts(length, measures):
    #print("getCuts start with length %s and measures %s" % (length, measures))
    listLength = len(measures)
    if listLength > 1:
        tempList = [(measures[-1] - measures[i]) for i in range(listLength) if (measures[-1] - measures[i]) > 0]
    else:
        tempList = []
    tempList.append(measures[-1])
    cut = length - measures[-1]   
    if cut > 0:
        tempList.append(cut)
    
    return countUnique(tempList)
    

def getCutList(cutsList, length, measures):
    #print("getCutsList2 start with cutsList %s, length %s and measures %s" % (cutsList, length, measures))
    for i in range(1, len(measures)+1):
        cutsList = mergeDict(cutsList, getCuts(length, measures[:i]))
        
    try:
        cutsList[length] = 1
    except:
        cutsList[length] += 1
    
    return cutsList
    
    
def countTotals(dictX, dictY):
    #print("countTotals start with dictX %s and dictY %s" % (dictX, dictY))
    result = 0
    
    if len(dictX) >= len(dictY):
        smaller = dictY
        bigger = dictX
    else:
        smaller = dictX
        bigger = dictY
    
    for key in smaller:
        try:
            result += bigger[key] * smaller[key]
        except:
            pass
             
    return result


cutsX = getCutList({}, w, measureX)
cutsY = getCutList({}, h, measureY)


print(countTotals(cutsX, cutsY))
