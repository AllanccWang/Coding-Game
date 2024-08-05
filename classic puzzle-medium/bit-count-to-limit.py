#https://www.codingame.com/training/medium/bit-count-to-limit
#BIT COUNT TO LIMIT
import sys
import math

def countSetBits(n) :
    # Ignore 0 as all the bits are unset
    n += 1
    # To store the powers of 2
    powerOf2 = 2
    # To store the result, it is initialized
    # with n/2 because the count of set
    # least significant bits in the integers
    # from 1 to n is n/2
    cnt = n // 2
    # Loop for every bit required to represent n
    while (powerOf2 <= n) :
        # Total count of pairs of 0s and 1s
        totalPairs = n // powerOf2
        # totalPairs/2 gives the complete
        # count of the pairs of 1s
        # Multiplying it with the current power
        # of 2 will give the count of
        # 1s in the current bit
        cnt += (totalPairs // 2) * powerOf2
        # If the count of pairs was odd then
        # add the remaining 1s which could
        # not be groupped together
        if (totalPairs & 1) :
            cnt += (n % powerOf2)
        else :
            cnt += 0
        powerOf2 <<= 1
    return cnt

n = int(input())
print(countSetBits(n))
