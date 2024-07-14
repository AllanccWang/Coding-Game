#https://www.codingame.com/training/hard/the-balanced-centrifuge-problem
#THE BALANCED CENTRIFUGE PROBLEM
#concept: Dynamic programming / Primes
require'prime'
n=gets.to_i
a=[0]*(n+1)
s=Prime.prime_division(n).map{_1[0]}
s.map{a[_1]=1}
#remove all number, which is a sum of prime divisors
#dynamic programming to store the numbers can be sum of factors
(2..n).each{|i|s.each{|c|a[i]=1 if a[i-c]==1} if a[i]==0}
#to balance k identical test tubes, 1 ≤ k ≤ n, in an n-hole centrifuge
#if both k and n-k can be expressed as a sum of prime divisors of n.
p (2..n).map{|i|a[i]==1&&a[n-i]==1?1:0}.sum+1
