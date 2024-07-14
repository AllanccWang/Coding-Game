'''
Given a certain integer n, we need a function big_primefac_div(), 
that give an array with the highest prime factor and the highest divisor (not equal to n).

Let's see some cases:

big_primefac_div(100) == [5, 50]
big_primefac_div(1969) == [179, 179]
If n is a prime number the function will output an empty list:

big_primefac_div(997) == []
If n is an negative integer number, it should be considered the division with the absolute number of the value.

big_primefac_div(-1800) == [5, 900]
If n is a float type, will be rejected if it has a decimal part with some digits different than 0. 
The output "The number has a decimal part. No Results". 
But n will be converted automatically to an integer if all the digits of the decimal part are 0.

big_primefac_div(-1800.00) == [5, 900]
big_primefac_div(-1800.1) == "The number has a decimal part. No Results"
Optimization and fast algorithms are a key factor to solve this kata.
'''
#https://www.codewars.com/kata/5646ac68901dc5c31a000022/python
#Give The Biggest Prime Factor And The Biggest Divisor Of A Number
import math

def maxPrimeFactors(n):
    maxPrime=-1
    
    while n%2==0:
        maxPrime=2
        n>>=1
    while n%3==0:
        maxPrime=3
        n=n/3
    #we have to iterate only for integers
    #who does not have prime factor 2 and 3
    for i in range(5,int(math.sqrt(n))+1,6):
        while n%i==0:
            maxPrime=i
            n=n/i
        while n%(i+2)==0:
            maxPrime=i+2
            n=n/(i+2)
         
    if n>4: maxPrime=n
    return int(maxPrime)

def big_primefac_div(n):
    
    if int(n)==n:
        n=int(abs(n))
        p=[]
        if maxPrimeFactors(n)==-1: return p
    
        for i in range(2,n//2+1):
            if n%i==0:
                p.append(n//i);
                p.append(maxPrimeFactors(n))
                break
                
        return p[::-1]
    
    else:
        return "The number has a decimal part. No Results"
