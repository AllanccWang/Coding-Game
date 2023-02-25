#https://www.codingame.com/training/hard/magic-count-of-numbers
#MAGIC COUNT OF NUMBERS

n, k = gets.split.map(&:to_i)
primes = gets.split.map(&:to_i)

p (1..k).reduce(0){|count, i|
count-(-1)**i*primes.combination(i).reduce(0){|sum, a| sum+n/a.reduce(&:*)}
}
